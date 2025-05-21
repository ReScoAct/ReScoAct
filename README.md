# ReScoAct: A Novel LLM-Based Agent Planning Paradigm via Reasoning, Scoring and Acting

In this paper, we propose ReScoAct, a novel LLM-based agent planning paradigm. In each planning epoch, the agent first generates $k$ candidate actions using an LLM, then evaluates redundancy and reliability scores of each action using historical- and prospective-based scoring strategies, respectively. A composite score is then computed via a weighted sum of the two scores, and the action with the highest composite score is selected for execution in the environment. This process is repeated iteratively until the task is completed or the execution action budget is exhausted. In summary, benefiting from the simple one-step-per-epoch interaction scheme, ReScoAct demonstrates broad applicability across a wide range of agent planning tasks.

<center> 
<img src='pic/flowsheet.png' width='800px'>
</center>


## Environment
See `requirements.txt`, some key dependencies are:
* python==3.11.0
* torch==2.2.0

## Usage
### Run on HotPotQA
Run the following code to run ReScoAct on the HotPotQA dataset with the default configuration.

```bash
cd HotPotQA_run
python run_script.py
```

### Run on ALFWorld
Run the following code to run ReScoAct on the ALFworld datastet with the default configuration.

```bash
cd ALFWorld_run
python ReScoAct.py
```