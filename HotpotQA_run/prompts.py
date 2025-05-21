Action_Reasoning_Prompt = """# Profile #
You are a question-answering robot. You are capable of taking a series of actions that are only in your <Action-Scope> to find a good answer to a question.

<Action-Scope>
The available actions are listed as follows:
    (1) Search[entity]: Search the exact entity on Wikipedia and return the first paragraph if it exists. If not, return some similar entities for searching. 
    (2) Lookup[keyword]: Return the next sentence that contains the keyword in the last passage successfully found by Search.
    (3) Finish[answer]: Return the answer and conclude the task.  
The using conditions of each action are listed as follows:
* From "Start", you need to begin with a "Search" action.
* From "Search", you can continue with "Search", switch to "Lookup", or proceed to "Finish".
* From "Lookup", you can continue with "Lookup", switch to "Search", or proceed to "Finish".
* The "Finish" is the final action where you provide the answer and the task is completed.
<\Action-Scope>

# Object # 
Now, your task is to propose three actions based on the current <State>. These actions should directly or indirectly contribute to answering the <Question>. The <State> includes a log of previously executed actions and their corresponding observations from the environment.

Your outputs should follow examples here:
{examples}
(END OF EXAMPLES)

<Question>
    {question}
<\Question>
<State>
    {state}
<\State>"""


Complete_ActionPath_Prompt = """# Profile #
You are a question-answering robot. You are capable of taking a series of actions that are only in your <Action-Scope> to find a good answer to a question.

<Action-Scope>
The available actions are listed as follows:
    (1) Search[entity]: Search the exact entity on Wikipedia and return the first paragraph if it exists. If not, return some similar entities for searching. 
    (2) Lookup[keyword]: Return the next sentence that contains the keyword in the last passage successfully found by Search.
    (3) Finish[answer]: Return the answer and conclude the task.  
The using conditions of each action are listed as follows:
* From "Start", you need to begin with a "Search" action.
* From "Search", you can continue with "Search", switch to "Lookup", or proceed to "Finish".
* From "Lookup", you can continue with "Lookup", switch to "Search", or proceed to "Finish".
* The "Finish" is the final action where you provide the answer and the task is completed.
<\Action-Scope>

# Object #
Your task is to plan a subsequent action path following <Pending-Plan> based on the current <State>. The completed action path should lead you to an effective answer for the <Question>. The <State> includes a log of previously executed action paths and their corresponding observations from the environment.

Your outputs should follow examples here:
{examples}
(END OF EXAMPLES)

<Question>
    {question}
<\Question>
<State>
    {state}
<\State>
<Pending-Plan>
    {pending_plan}
<\Pending-Plan>"""


P_Score_ActionPaths_Prompt = """# Object #
You task is to assist a question-answering robot by scoring the reliability of its planned candidate action paths for answering the <Question>, based on its current <State>. Reliability reflects the likelihood that an action path will ultimately lead to successful task completion. The <State> includes a log of previously executed action paths and their corresponding observations from the environment. <Action-Scope> records the robot's available action descriptions and transition rules.  
#### Scoring Guidelines ####
* A score of **0** indicates the action path is entirely unfeasible, and the robot cannot find a good answer at the end.
* A score of **10** indicates the action path is fully reliable, and the robot can ultimately provide a good answer to the question.

<Action-Scope>
The available actions are listed as follows:
    (1) Search[entity]: Search the exact entity on Wikipedia and return the first paragraph if it exists. If not, return some similar entities for searching. 
    (2) Lookup[keyword]: Return the next sentence that contains the keyword in the last passage successfully found by Search.
    (3) Finish[answer]: Return the answer and conclude the task.  
The using conditions of each action are listed as follows:
* From "Start", you need to begin with a "Search" action.
* From "Search", you can continue with "Search", switch to "Lookup", or proceed to "Finish".
* From "Lookup", you can continue with "Lookup", switch to "Search", or proceed to "Finish".
* The "Finish" is the final action where you provide the answer and the task is completed.
<\Action-Scope>

Here are some examples:
{examples}
(END OF EXAMPLES)

<Question>
    {question}
<\Question>
<State>
    {state}
<\State>
<Candidate-ActionPath>
    {candidate_actionpaths}
<\Candidate-ActionPath>"""


H_Score_Actions_Prompt = """# Object #
Your task is to assist a question-answering robot by scoring the redundancy of its condidate next actions for answering the <Question>, based on the current <State>. Redundancy measures how likely a action’s expected observation has already been covered by prior actions. The robot operates within a defined <Action-Scope> and executes sequential actions to find an answer. The <State> includes a log of previously executed actions and their corresponding observations from the environment.
#### Scoring Guidelines ####
* A score of **0** indicates the action is completely redundant, offering no new or useful information for answering the question.
* A score of **10** indicates the action is entirely necessary and will significantly help the robot gather missing information to answer the question.

<Action-Scope>
The available actions are listed as follows:
    (1) Search[entity]: Search the exact entity on Wikipedia and return the first paragraph if it exists. If not, return some similar entities for searching. 
    (2) Lookup[keyword]: Return the next sentence that contains the keyword in the last passage successfully found by Search.
    (3) Finish[answer]: Return the answer and conclude the task.  
The using conditions of each action are listed as follows:
* From "Start", you need to begin with a "Search" action.
* From "Search", you can continue with "Search", switch to "Lookup", or proceed to "Finish".
* From "Lookup", you can continue with "Lookup", switch to "Search", or proceed to "Finish".
* The "Finish" is the final action where you provide the answer and the task is completed.
<\Action-Scope>

Here are some examples:
{examples}
(END OF EXAMPLES)

<Question>
    {question}
<\Question>
<State>
    {state}
<\State>
<Candidate-Next-Action>
    {candidate_actions}
<\Candidate-Next-Action>"""