import os, sys
import re
from functools import partial

import numpy as np

from _prompt import *
from llms import get_llm_backend

# os.environ["ALFWORLD_DATA"] = "/data/xuxiaoming/codesource/astaragent/src/cache"

prefixes = {
    'pick_and_place': 'put',
    'pick_clean_then_place': 'clean',
    'pick_heat_then_place': 'heat',
    'pick_cool_then_place': 'cool',
    'look_at_obj': 'examine',
    'pick_two_obj': 'puttwo'
}

game2prompts = {
    "put": {
        "proposing": partial(Action_Reasoning_Prompt.format, task_action_scope=ALF_Put_ActionScope, examples=ALF_Put_Reasoning_Examples),
        "planning": partial(Complete_ActionPath_Prompt.format, task_action_scope=ALF_Put_ActionScope, examples=ALF_Put_Planning_Examples),
        "h_scoring": partial(P_Score_ActionPaths_Prompt.format, task_action_scope=ALF_Put_ActionScope, examples=ALF_Put_P_Scoring_Examples),
        "g_scoring": partial(H_Score_Actions_Prompt.format, task_action_scope=ALF_Put_ActionScope, examples=ALF_Put_H_Scoring_Examples),
    },
    "clean": {
        "proposing": partial(Action_Reasoning_Prompt.format, task_action_scope=ALF_Clean_ActionScope, examples=ALF_Clean_Reasoning_Examples),
        "planning": partial(Complete_ActionPath_Prompt.format, task_action_scope=ALF_Clean_ActionScope, examples=ALF_Clean_Planning_Examples),
        "h_scoring": partial(P_Score_ActionPaths_Prompt.format, task_action_scope=ALF_Clean_ActionScope, examples=ALF_Clean_P_Scoring_Examples),
        "g_scoring": partial(H_Score_Actions_Prompt.format, task_action_scope=ALF_Clean_ActionScope, examples=ALF_Clean_H_Scoring_Examples),
    },
    "heat": {
        "proposing": partial(Action_Reasoning_Prompt.format, task_action_scope=ALF_Heat_ActionScope, examples=ALF_Heat_Reasoning_Examples),
        "planning": partial(Complete_ActionPath_Prompt.format, task_action_scope=ALF_Heat_ActionScope, examples=ALF_Heat_Planning_Examples),
        "h_scoring": partial(P_Score_ActionPaths_Prompt.format, task_action_scope=ALF_Heat_ActionScope, examples=ALF_Heat_P_Scoring_Examples),
        "g_scoring": partial(H_Score_Actions_Prompt.format, task_action_scope=ALF_Heat_ActionScope, examples=ALF_Heat_H_Scoring_Examples),
    },
    "cool": {
        "proposing": partial(Action_Reasoning_Prompt.format, task_action_scope=ALF_Cool_ActionScope, examples=ALF_Cool_Reasoning_Examples),
        "planning": partial(Complete_ActionPath_Prompt.format, task_action_scope=ALF_Cool_ActionScope, examples=ALF_Cool_Planning_Examples),
        "h_scoring": partial(P_Score_ActionPaths_Prompt.format, task_action_scope=ALF_Cool_ActionScope, examples=ALF_Cool_P_Scoring_Examples),
        "g_scoring": partial(H_Score_Actions_Prompt.format, task_action_scope=ALF_Cool_ActionScope, examples=ALF_Cool_H_Scoring_Examples),
    },
    "examine": {
        "proposing": partial(Action_Reasoning_Prompt.format, task_action_scope=ALF_Examine_ActionScope, examples=ALF_Examine_Reasoning_Examples),
        "planning": partial(Complete_ActionPath_Prompt.format, task_action_scope=ALF_Examine_ActionScope, examples=ALF_Examine_Planning_Examples),
        "h_scoring": partial(P_Score_ActionPaths_Prompt.format, task_action_scope=ALF_Examine_ActionScope, examples=ALF_Examine_P_Scoring_Examples),
        "g_scoring": partial(H_Score_Actions_Prompt.format, task_action_scope=ALF_Examine_ActionScope, examples=ALF_Examine_H_Scoring_Examples),
    },
    "puttwo": {
        "proposing": partial(Action_Reasoning_Prompt.format, task_action_scope=ALF_Puttwo_ActionScope, examples=ALF_Puttwo_Reasoning_Examples),
        "planning": partial(Complete_ActionPath_Prompt.format, task_action_scope=ALF_Puttwo_ActionScope, examples=ALF_Puttwo_Planning_Examples),
        "h_scoring": partial(P_Score_ActionPaths_Prompt.format, task_action_scope=ALF_Puttwo_ActionScope, examples=ALF_Puttwo_P_Scoring_Examples),
        "g_scoring": partial(H_Score_Actions_Prompt.format, task_action_scope=ALF_Puttwo_ActionScope, examples=ALF_Puttwo_H_Scoring_Examples),
    },
}

class LLMAgentInterface:
    def __init__(self, llm):
        self.model = llm
        self.session = {}
    
    def planning_actions(self, game_type, situation):
        # 1. Inference
        _prompt = game2prompts[game_type]["proposing"]
        llm_response = self.model.run(
            max_tokens=512,
            prompt=_prompt(gaming_log = situation,)
        )
        print(_prompt(gaming_log = situation,))
        print(llm_response)
        n_access = 1
        # 2. parse
        # parse the think text
        think_pattern = r'Think: (.*?)\n'
        think_match = re.search(think_pattern, llm_response)
        think_content = think_match.group(1)
        # prase the Next-Action text
        action_pattern = r'Next-Action-\d+: (.*?)(\n|$)'
        action_matches = re.findall(action_pattern, llm_response)
        action_matches = [m[0] for m in action_matches]
        print("\t".join(["* {}".format(a) for a in action_matches]))
        return think_content, action_matches, n_access, llm_response.strip()
    
    def H_scoring(self, game_type, situation, think, candidate_actions):
        n_access = 0
        responses = []
        scores = []
        _prompt1 = game2prompts[game_type]["planning"]
        for action in candidate_actions:
            round_response = []
            # 1. complete pending-paths
            llm_response_1 = self.model.run(
                max_tokens=512,
                prompt=_prompt1(
                    gaming_log = situation,
                    think = f"> Think: {think}",
                    action = action,
                )
            )
            print(llm_response_1)
            round_response.append(llm_response_1)
            n_access += 1
            # parse the path

            # 2. scoring
            _prompt2 = game2prompts[game_type]["h_scoring"]
            llm_response_2 = self.model.run(
                max_tokens=512,
                prompt=_prompt2(
                    gaming_log = situation,
                    pending_action = f"> Think: {think}\n> Action: {action}",
                    completed_actions = llm_response_1,
                )
            )
            print(llm_response_2)
            round_response.append(llm_response_2)
            n_access += 1
            # parse scores
            score_pattern = r'\[score\]:\s*(\d+)'
            score = re.search(score_pattern, llm_response_2)
            scores.append(score.group(1))
            responses.append(round_response)

        scores = np.array([int(s) for s in scores])
        print("H scores:\n{}".format("\t".join(["* {}".format(s) for s in scores])))
        return scores, n_access, responses

    def G_scoring(self, game_type, situation, think, candidate_actions):
        # 1. inference
        _prompt = game2prompts[game_type]["g_scoring"]
        llm_response = self.model.run(
            max_tokens=512,
            prompt=_prompt(
                gaming_log = situation,
                think = think,
                action1 = candidate_actions[0],
                action2 = candidate_actions[1],
                action3 = candidate_actions[2],
            )
        )
        print(llm_response)
        n_access = 1
        # parse scores
        score_pattern = r'\[score\]:\s*(\d+)'
        scores = re.findall(score_pattern, llm_response)
        scores = np.array([int(s) for s in scores])
        print("G scores:\n{}".format("\t".join(["* {}".format(s) for s in scores])))
        return scores, n_access, llm_response


def process_ob(ob):
    if ob.startswith('You arrive at loc'):
        ob = ob[ob.find('. ')+2:]
    return ob

def process_ac(action):
    action = action.strip('\n').strip().replace('\n', '')
    if " in " in action:
        action = action.replace(" in ", " in/on ")
    elif " on " in action:
        action = action.replace(" on ", " in/on ")
    return action

class ReScoAct():
    def __init__(self, llm_interface, game_type, ob):
        self.backbone: LLMAgentInterface = llm_interface
        self.H_score_weight = 1
        self.G_score_weight = 1
        self._reset_agent(game_type, ob)
    
    def _reset_agent(self, game_type, ob):
        self.situation = ob + "\n>Action: Start"
        self.pre_action = "start"
        
        self.game_type = game_type
        
        self.h_scoring = False
        self.n_access = 0
        self.exexute_log = []

    def print_inprocess_info(self):
        print("============ Agent Running Log ============")
        num_inference_tip =  "🌟 Num Inference: x{:>3d}".format(self.n_access)
        action_trajectory_tip = "\n🌟 Executing Log:\n{}".format(self.situation)
        print("===========================================")
    
    def _planning(self):
        _responses = []
        # 1. planning
        print("--- predicting next actions ---")
        _think, next_action_list, n_access, llm_response = self.backbone.planning_actions(
            self.game_type,
            self.situation, 
        )
        _responses.append(llm_response)
        self.n_access += n_access

        # 2. scoring
        print("--- A* scoring on actions ---")
        # a. h-score
        # print(self.h_scoring)
        if self.h_scoring:
            h_scores, n_access, llm_response = self.backbone.H_scoring(
                self.game_type,
                self.situation,
                _think,
                next_action_list[:3],
            )
            self.n_access += n_access
            _responses.append(llm_response)
        else:
            h_scores = np.array([0, 0, 0])
        # b. g-score
        g_scores, n_access, llm_response = self.backbone.G_scoring(
            self.game_type,
            self.situation,
            _think,
            next_action_list[:3],
        )
        self.n_access += n_access
        _responses.append(llm_response)

        # 3. pick the best action
        f_scores = self.H_score_weight*h_scores + self.G_score_weight*g_scores
        _action_id = np.argmax(f_scores)
        _action = next_action_list[_action_id]

        self.exexute_log.append({
            "Agent": self.situation,
            "LLM": _responses,
            "Final Action": _action
        })
        return _action, _think

    def run(self, max_step=10):
        epoch_counter = 0
        while epoch_counter < max_step:
            try:
                print(f">>> {epoch_counter:>3d}-th planning step >>>")
                # 1. planning the next action
                _action, _think = self._planning()
                print(f"The Current Action: {_action}")
                # 2. interact with environment
                action:str = process_ac(_action)
                observation, reward, done, info = env.step([action])
                observation, reward, done = process_ob(observation[0]), info['won'][0], done[0]

                # 3. update
                if self.pre_action.startswith("take"):
                    self.h_scoring = True

                if self.pre_action.startswith("go") and action.startswith("open"):
                    self.situation += "\n"
                    self.situation += f"> Action: {action}\n"
                    self.situation += observation
                else:
                    self.situation += "\n\n"
                    self.situation += f"> Think: {_think}\n"
                    self.situation += f"> Action: {action}\n"
                    self.situation += observation

                self.pre_action = action
                self.print_inprocess_info()
                if done:
                    return reward, self.situation

                epoch_counter += 1
            except IndexError:
                continue
        # return result
        return 0, self.situation

def set_log_file(fname):
    import subprocess, sys, os
    # set log file
    # sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)
    tee = subprocess.Popen(['tee', fname], stdin=subprocess.PIPE)
    os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
    os.dup2(tee.stdin.fileno(), sys.stderr.fileno())

if __name__ == "__main__":
    import json
    import yaml
    import pandas as pd
    from alfworld.agents import environment
    
    model_id = "deepseek-chat"
    resume = False
    game_num = 134
    split = "eval_out_of_distribution"

    log_root = "agentlogs/rescoact_normal_deepseek/model_id_{model_id}_test_134/"
    os.makedirs(log_root, exist_ok=True)

    with open('ALFWorld_run/base_config.yaml') as reader:
        config = yaml.safe_load(reader)

    env = getattr(environment, config["env"]["type"])(config, train_eval=split)
    env = env.init_env(batch_size=1)

    # prepare llm
    llm = get_llm_backend(model_id)
    llm_interface = LLMAgentInterface(llm)

    if resume:
        with open("running_checkpoint_deepseek.json", 'r') as resumefile:
            checkpoint_dict = json.load(resumefile)
            cnts = checkpoint_dict['cnts']
            rs = checkpoint_dict['rs']
            start = checkpoint_dict['last_id'] + 1
    else:
        cnts = [0] * 6
        rs = [0] * 6
        start = 0

    for task_id in range(game_num):
        ob, info = env.reset()
        if task_id < start:
            continue

        ob = ob[0].split('\n\n')[1:]
        name = '/'.join(info['extra.gamefile'][0].split('/')[-3:-1])

        print("##### task:{:>3d} #####\n🚀 name: {}\n########################".format(task_id, name))
        set_log_file(f"screencuts_deepseek/output{task_id}.txt")

        for i, (k, v) in enumerate(prefixes.items()):
            if name.startswith(k):
                print(k, v)
                agent = ReScoAct(llm_interface, v, '\n'.join(ob))
                r, traj = agent.run(30)

                rs[i] += r
                cnts[i] += 1

                result_entry = {
                    "game_type": v,
                    "task": ob[1],
                    "is_finish": bool(r),
                    "num_query": agent.n_access,
                    "running_log": agent.situation.strip('\n'),
                    "llm_output_log": agent.exexute_log,
                }
                print("🌺 If Finished: {}\n🌺 num queries: {}".format(bool(r), agent.n_access))


                with open(f"{log_root}/task{task_id}_log.json", 'w') as logfile:
                    json.dump(result_entry, logfile, indent=2, ensure_ascii=False)
                
                del agent
                break
    
        with open("running_checkpoint_deepseek.json", 'w') as checkpointfile:
            checkpoint = {
                "cnts": cnts,
                "rs": rs,
                "last_id": task_id,
            }
            json.dump(checkpoint, checkpointfile, indent=2)

        rates = []
        for j in range(6):
            if cnts[j] != 0:
                rates.append(rs[j]/cnts[j])
            else:
                rates.append(0.)
        temp = pd.DataFrame([rs, cnts, rates], columns=["put", "clean", "heat", "cool", "examine", "puttwo"])
        
        print(temp)
        print("🔥 average task success rate: {}".format(sum(rs)/sum(cnts)))

        
        