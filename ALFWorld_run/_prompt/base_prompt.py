Action_Reasoning_Prompt = """# Profile #
You are a household robot. You are capable of interacting with a household by taking actions that are only in your <Action-Scope> to solve a task.

{task_action_scope}

# Object #
Use the Think step to understand the current situation and determine a course of your next moves. Then propose three possible **next steps** to progress the task.

Here are some examples:
{examples}

Here is the task.
{gaming_log}
[Propose]:"""


Complete_ActionPath_Prompt = """# Profile #
You are a household robot. You are capable of interacting with a household by taking actions that are only in your <Action-Scope> to solve a task.

{task_action_scope}

# Object #
Based on the situation, plan **subsequent moves** following the pending action. The completed action path guides you to solve the task effectively. 

Here are some examples:
{examples}

Here is the task.
{gaming_log}

{think}
{action}
[subsequent moves]:"""


P_Score_ActionPaths_Prompt = """# Object #
Assist a household robot by scoring the reliability of [subsequent moves] planned for solving the task, based on the situation. Reliability reflects the likelihood that an action path will ultimately lead to successful task completion. The situation includes a log of previously executed actions and their corresponding observations from the household. <Action-Scope> records the robot's available action descriptions and transition rules.

# Scoring Guidelines #
* A score of **0** indicates the action path is entirely unfeasible, and the robot cannot complete the task finally.
* A score of **10** indicates the action path is fully reliable, and the robot can effectively solve the task at the end.

{task_action_scope}

Here are some examples:
{examples}

Here is the task.
{gaming_log}

[subsequent moves]:
{pending_action}

{completed_actions}

[reasoning]:

[score]:"""


H_Score_Actions_Prompt = """# Object #
Assist a household robot by scoring the redundancy of three possible [next steps] planned for solving the task, based on the situation. Redundancy measures how likely a action’s expected observation has already been covered by prior actions. <Action-Scope> records the robot's available action descriptions and transition rules. The situation includes a log of previously executed actions and their corresponding observations from the household.

# Scoring Guidelines #
* A score of **0** indicates the action is completely redundant or unfeasible, and will making no progress toward solving the task.
* A score of **10** indicates the action is absolutely necessary, and will significantly contribute to advancing the task.

{task_action_scope}

Here are some examples:
{examples}

Here is the task.
{gaming_log}

{think}
[next stpes]:
> Next-Action-1: {action1}
[reasoning]:
[score]:

> Next-Action-2: {action2}
[reasoning]:
[score]:

> Next-Action-3: {action3}
[reasoning]:
[score]:"""