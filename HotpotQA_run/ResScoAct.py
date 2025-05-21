import re
import string
from collections import Counter

import numpy as np
from dotenv import load_dotenv
from langchain_community.docstore import Wikipedia
from langchain.agents.react.base import DocstoreExplorer

from prompts import Action_Reasoning_Prompt, Complete_ActionPath_Prompt, \
    P_Score_ActionPaths_Prompt, H_Score_Actions_Prompt
from _prompt.examples import Action_Reasoning_Examples, Complete_ActionPath_Examlpes, \
    P_Score_ActionPaths_Examples, H_Score_Actions_Examples

load_dotenv()

def f1_score(prediction, ground_truth):
    normalized_prediction = normalize_answer(prediction)
    normalized_ground_truth = normalize_answer(ground_truth)

    ZERO_METRIC = (0, 0, 0)

    if normalized_prediction in ['yes', 'no', 'noanswer'] and normalized_prediction != normalized_ground_truth:
        return ZERO_METRIC
    if normalized_ground_truth in ['yes', 'no', 'noanswer'] and normalized_prediction != normalized_ground_truth:
        return ZERO_METRIC
  
    prediction_tokens = normalized_prediction.split()
    ground_truth_tokens = normalized_ground_truth.split()
    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        return ZERO_METRIC
    precision = 1.0 * num_same / len(prediction_tokens)
    recall = 1.0 * num_same / len(ground_truth_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1, precision, recall


def normalize_answer(s):
    def remove_articles(text):
        return re.sub(r"\b(a|an|the)\b", " ", text)
    
    def white_space_fix(text):
        return " ".join(text.split())
    
    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)
    
    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def is_correct(answer, key):
    return normalize_answer(answer) == normalize_answer(key)


def format_step(step: str) -> str:
    return step.strip('\n').strip().replace('\n', '')


class BaseActionScope:
    def __init__(self, docstore = Wikipedia()):
        self.search_results_num = 3
        self.docstore = DocstoreExplorer(docstore) # Search, Lookup
                
class LLMAgentInterface:
    def __init__(self, llm):
        self.model = llm
        self.session = {}
    
    def planning_actions(self, question, state):
        # 1. Inference
        llm_response = self.model.run(
            max_tokens=512,
            prompt=Action_Reasoning_Prompt.format(
                examples = Action_Reasoning_Examples,
                question = question,
                state = state,
            )
        )
        n_access = 1
        # 2. parse
        actions = re.findall(r'\[Action-[a-z]\]:\s*(\w+\[.*?\])', llm_response)
        print("\t".join(["* {}".format(a) for a in actions]))
        print(llm_response)
        return actions, n_access, llm_response.strip()
    
    def H_scoring(self, question, state, current_path, candidate_actions):
        n_access = 0
        responses = []
        # 1. complete pending-paths
        candidate_paths = []
        for action in candidate_actions:
            pending_path = "{}->{}".format(current_path, action)
            if action.lower().startswith("finish"):
                candidate_paths.append(pending_path)
            else:
                # inference
                print(Complete_ActionPath_Prompt.format(
                        examples = Complete_ActionPath_Examlpes,
                        question = question,
                        state = state,
                        pending_plan = pending_path,
                    ))
                llm_response = self.model.run(
                    max_tokens=512,
                    prompt=Complete_ActionPath_Prompt.format(
                        examples = Complete_ActionPath_Examlpes,
                        question = question,
                        state = state,
                        pending_plan = pending_path,
                    )
                )
                print(llm_response)
                responses.append(llm_response)
                n_access += 1
                # parse the path
                path_pattern = r'Start\[\]->(.*)'
                pending_path = re.search(path_pattern, llm_response)
                candidate_paths.append(pending_path.group(0))
        # 2. scoring
        llm_response = self.model.run(
            max_tokens=512,
            prompt=P_Score_ActionPaths_Prompt.format(
                examples = P_Score_ActionPaths_Examples,
                question = question,
                state = state,
                candidate_actionpaths = "\n\n    ".join(["[{}] {}".format(chr(97+i), p) for i, p in enumerate(candidate_paths)])
            )
        )
        responses.append(llm_response)
        n_access += 1
        # parse scores
        score_pattern = r'\[Score\]:\s*(\d+)'
        scores = re.findall(score_pattern, llm_response)
        scores = np.array([int(s) for s in scores])
        print("H scores:\n{}".format("\t".join(["* {}".format(s) for s in scores])))
        return scores, n_access, responses

    def G_scoring(self, question, state, candidate_actions):
        # 1. inference
        llm_response = self.model.run(
            max_tokens=512,
            prompt=H_Score_Actions_Prompt.format(
                examples = H_Score_Actions_Examples,
                question = question,
                state = state,
                candidate_actions = "\n\n    ".join(["[{}] {}".format(chr(97+i), p) for i, p in enumerate(candidate_actions)])
            )
        )
        n_access = 1
        # parse scores
        score_pattern = r'\[Score\]:\s*(\d+)'
        scores = re.findall(score_pattern, llm_response)
        scores = np.array([int(s) for s in scores])
        print("G scores:\n{}".format("\t".join(["* {}".format(s) for s in scores])))
        # print(llm_response)
        return scores, n_access, llm_response


class ReScoAct(BaseActionScope):
    def __init__(self, llm_interface, question, docstore=Wikipedia()):
        super().__init__(docstore)
        self.backbone: LLMAgentInterface = llm_interface
        self.question = question
        self.H_score_weight = 0.75
        self.G_score_weight = 0.25
        self._reset_agent()
    
    def _reset_agent(self):
        self.n_access = 0
        self.finish = False
        self.answer = None
        self.guess = None

        self.observations = ["[observation 0]: The planning agent starts planning."]
        self.actionpath = "Start[]"
        self.pre_action = "Start"

        self.state_action = [
            "[Action-0]: Start[]", 
            "[Observation-0]: The planning agent starts planning."
            ]
        self.state_actionpath = [
            "[ActionPath-0]: Start[]", 
            "[Observation-0]: The planning agent starts planning."
            ]
        
        self.session = []
    
    def print_inprocess_info(self):
        print("=========== Agent Aswering Info ===========")
        user_question_tip = "🌟 User question: {}".format(self.question)
        action_trajectory_tip = "\n🌟 ActionPath: {}".format(self.actionpath)
        observations_tip = "\n🌟 Obtained Observations:"
        for obv in self.observations:
            obv = '\n' + obv 
            observations_tip += obv
        num_inference_tip =  "\n🌟 Num Inference: x{:>3d}".format(self.n_access)
        print(user_question_tip, action_trajectory_tip, observations_tip, num_inference_tip)
        print("===========================================")
    
    def _planning(self):
        _responses = []
        # 1. planning
        print("--- predicting next actions ---")
        next_action_list, n_access, llm_response = self.backbone.planning_actions(
            self.question,
            '\n    '.join(self.state_action), 
        )
        self.n_access += n_access
        _responses.append(llm_response)
        # recording guess answer
        for _action in next_action_list:
            if _action.lower().startswith("finish"):
                self.guess = re.findall(r'\[([^\]]+)\]', _action)[0]

        # 2. scoring
        print("--- A* scoring on actions ---")
        # a. h-score
        h_scores, n_access, llm_response = self.backbone.H_scoring(
            self.question, 
            '\n    '.join(self.state_actionpath), 
            self.actionpath,
            next_action_list,
        )
        self.n_access += n_access
        _responses.append(llm_response)
        # b. g-score
        g_scores, n_access, llm_response = self.backbone.G_scoring(
            self.question,
            '\n    '.join(self.state_action),
            next_action_list,
        )
        self.n_access += n_access
        _responses.append(llm_response)

        # 3. pick the best action
        f_scores = self.H_score_weight*h_scores + self.G_score_weight*g_scores
        _action_id = np.argmax(f_scores)
        _action = next_action_list[_action_id]
        self.session.append({
            "Agent": '\n'.join(self.state_actionpath),
            "LLM": _responses,
            "Final Action": _action
        })
        return _action

    def run(self, max_step=10):
        epoch_counter = 0
        while epoch_counter < max_step:
            try:
                print(f">>> {epoch_counter:>3d}-th planning step >>>")
                # 1. planning the next action
                _action = self._planning()
                # _action = "Retrieve[Matt Groening]"
                print(f"The Current Action: {_action}")

                # 2. interact with environment
                if _action.lower().startswith("finish"):
                    self.finish = True
                    self.answer = re.findall(r'\[([^\]]+)\]', _action)[0]
                    return self.answer
                
                elif _action.lower().startswith("search"):
                    try:
                        self.pre_action = "Search"
                        argument = re.findall(r'\[([^\]]+)\]', _action)[0]
                        _observation = format_step(self.docstore.search(argument))
                    except Exception as e:
                        _observation = "Could not find that page, please try again."
                        print(e,'\n', _observation)
                elif _action.lower().startswith("lookup"):
                    argument = re.findall(r'\[([^\]]+)\]', _action)[0]
                    if self.pre_action == "Search":
                        try:
                            _observation = format_step(self.docstore.lookup(argument))
                        except ValueError:
                            _observation = "The last page Retrieved was not found, so you cannot Lookup a keyword in it. Please try one of the similar pages given."
                    elif self.pre_action == "Start":
                        _observation = "You cannot Lookup a keyword without performing 'Retrieve' or 'Search' before. Please try 'Retrieve' or 'Search' first."
                else:
                    _observation = 'Invalid Action. Valid Actions are Lookup[<topic>] Search[<topic>] Retrieve[<topic>] and Finish[<answer>].'
                    print(_action, _observation)

                # 3. update
                if not _observation.startswith("Invalid Action."):
                    _actionpath = self.actionpath + f"->{_action}"
                    _observation = "[Observation-{}]: {}".format(len(self.observations), _observation)
                    
                    self.actionpath = _actionpath
                    self.observations.append(_observation)

                    self.state_action.append("[Action-{}]: {}".format(len(self.observations), _action))
                    self.state_action.append(_observation)
                    self.state_actionpath.append("[ActionPath-{}]: {}".format(len(self.observations), _actionpath))
                    self.state_actionpath.append(_observation)
                
                self.print_inprocess_info()
                epoch_counter += 1
            except IndexError:
                continue
    
        # return an answer
        self.finish = False
        self.answer = self.guess
        return self.answer
