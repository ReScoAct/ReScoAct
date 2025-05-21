import os
import json
import joblib
import argparse
from functools import partial

from llms import get_llm_backend
from HotpotQA_run.ResScoAct import ReScoAct, LLMAgentInterface, is_correct

def set_log_file(fname):
    import subprocess, sys, os
    # set log file
    # sys.stdout = os.fdopen(sys.stdout.fileno(), 'wb', 0)
    tee = subprocess.Popen(['tee', fname], stdin=subprocess.PIPE)
    os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
    os.dup2(tee.stdin.fileno(), sys.stderr.fileno())

def arg_parser():
    parser = argparse.ArgumentParser(description='Parsing the input of agents, llms and llm context length.')
    parser.add_argument("--model_id", type=str, help="Name of the llm", default="deepseek-chat")
    parser.add_argument("--max_context_len", type=int, help="Maximum context length", default=1700)
    parser.add_argument("--mode", type=str,  help="train or test",default="test")   #required=True,
    parser.add_argument("--level", type=str, help="easy, medium or hard", default="easy")#required=True,
    parser.add_argument("--save_root", type=str, help="output path")#required=True,
    parser.add_argument("--p", type=float, help="probability of hallucination", default=0.1)
    parser.add_argument("-resume", action='store_true', help="restart from checkpoint", default="False")#
    args = parser.parse_args()
    return args

def main(cong):
    # create logfile dir
    os.makedirs(cong.save_dir, exist_ok=True)
    set_log_file(os.path.join(cong.save_dir, "screen_cut.txt"))

    # load dataset
    if cong.mode == "test":
        # level: easy, medium or hard
        test_dataset = joblib.load(f'HotpotQA_run/data/test/{cong.level}.joblib').reset_index(drop = True)
        task_instructions = [(row['question'], row['answer']) for _, row in test_dataset.iterrows()]
    elif cong.mode == "train":
        hotpot = json.load(open("HotpotQA_run/data/train/hotpot_train.json"))
        task_instructions = [(row['question'], row['answer']) for row in hotpot]

    # prepare llm
    llm = get_llm_backend(cong.model_id)
    # make llm as a decision-maker of A*agent 
    llm_interface = LLMAgentInterface(llm)

    # resume
    if cong.resume:
        with open("checkpoint.json", 'r') as resumefile:
            checkpoint_dict = json.load(resumefile)
            start_task_id = checkpoint_dict['task_id']+1 if checkpoint_dict['is_complete'] else checkpoint_dict['task_id']
            succ_task_id = checkpoint_dict['succ_task_id']
    else:
        start_task_id = 0
        succ_task_id = []
        
    agentmaker = partial(ReScoAct, llm_interface=llm_interface,)
    for i, (question, answer) in enumerate(task_instructions[start_task_id:], start_task_id):
        if i in succ_task_id:  # MODIFIED: Check if task is already successful
            print(f"Skipping task {i} as it has already been completed successfully.")
            continue  # MODIFIED: Skip the task
        print("##### Question {:>3d} #####\n🚀 User Question:\n{}\n🌕 Standard Answer:{}\n########################".format(i, question, answer))
        agent = agentmaker(question=question)
        agent.run()
        agent.answer = "None" if agent.answer is None else agent.answer
        print("🌺 If Finished: {}\n🌺 Agent Answer: {}\n🌕 Standard Answer:{}".format(agent.finish, agent.answer, answer))

        task_complete = False
        if is_correct(agent.answer, answer):
            succ_task_id.append(i)
            task_complete = True

        # save
        with open(os.path.join(cong.save_dir, f"question{i}_task_log.json"), 'w') as logfile:
            task_log = {
                "User Question": question,
                "Standard Answer": answer,
                "Is Finished": agent.finish,
                "LLM Answer": agent.answer,
                "Query Num": agent.n_access,
                "Action Num": len(agent.observations),
                "Session Info": agent.session,
            }
            json.dump(task_log, logfile, indent=2)

        with open("checkpoint.json", 'w') as checkpointfile:
            checkpoint = {
                "task_id": i,
                "is_complete": task_complete,
                "succ_task_num":len(succ_task_id),
                "succ_task_id":succ_task_id,
            }
            json.dump(checkpoint, checkpointfile, indent=2)

        del agent

if __name__ == "__main__":
    cong = arg_parser()
    cong.save_dir = os.path.join(
        "save_dir", "model_id_{}_mode_{}_level_{}".format(cong.model_id, cong.mode, cong.level)
    )
    main(cong)