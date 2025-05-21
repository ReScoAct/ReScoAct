ALF_Put_ActionScope = """<Action-Scope>
The available actions are as follows:
    (1) go to receptacle 
    (2) take object from receptacle 
    (3) put object in/on receptacle 
    (4) open receptacle
The transition rules between actions are listed as follows:
* You must go to a receptacle before opening it, if it is closed.
* To take an object from a receptacle, you must either be at its location or open it first if it is closed.
* You must pick take an object before moving to a new receptacle where the object will be placed. 
* You must put an object in/on a receptacle after either going to the location of the receptacle or taking an object with you.
<\Action-Scope>"""


ALF_Examine_ActionScope = """<Action-Scope>
The available actions are as follows:
    (1) go to receptacle
    (2) take object from receptacle
    (3) use receptacle
    (4) open receptacle
The transition rules between actions are listed as follows:
* You must go to a receptacle before opening it, if it is closed.
* To take an object from a receptacle, you must either be at its location or open it first if it is closed.
* To use an receptacle, you must first go to its location.
<\Action-Scope>"""


ALF_Clean_ActionScope = """<Action-Scope>
The available actions are as follows:
    (1) go to receptacle 
    (2) take object from receptacle
    (3) open receptacle
    (4) put object in/on receptacle 
    (5) clean object with receptacle
The transition rules between actions are listed as follows:
* You must go to a receptacle before opening it, if it is closed.
* To take an object from a receptacle, you must either be at its location or open it first if it is closed.
* You must put an object in or on a receptacle after either going to the location of the receptacle or taking an object with you.
* To clean an object using a receptacle, the object must first be placed in/on that receptacle.
<\Action-Scope>"""


ALF_Heat_ActionScope = """<Action-Scope>
The available actions are as follows:
    (1) go to receptacle
    (2) take object from receptacle
    (3) open receptacle
    (4) put object in/on receptacle
    (5) heat object with receptacle
The transition rules between actions are listed as follows:
* You must go to a receptacle before opening it, if it is closed.
* To take an object from a receptacle, you must either be at its location or open it first if it is closed.
* You must put an object in/on a receptacle after either going to the location of the receptacle or taking an object with you.
<\Action-Scope>"""


ALF_Cool_ActionScope = """<Action-Scope>
The available actions are as follows:
    (1) go to receptacle 
    (2) take object from receptacle
    (3) open receptacle
    (4) put object in/on receptacle 
    (5) cool object with receptacle
The transition rules between actions are listed as follows:
* You must go to a receptacle before opening it, if it is closed.
* To take an object from a receptacle, you must either be at its location or open it first if it is closed.
* You must put an object in/on a receptacle after either going to the location of the receptacle or taking an object with you. 
<\Action-Scope>"""


ALF_Puttwo_ActionScope = """<Action-Scope>
The available actions are as follows:
    (1) go to receptacle 
    (2) take object from receptacle 
    (3) put object in/on receptacle 
    (4) open receptacle
The transition rules between actions are listed as follows:
* You must go to a receptacle before opening it, if it is closed.
* To take an object from a receptacle, you must either be at its location or open it first if it is closed.
* You must pick take an object before moving to a new receptacle where the object will be placed. 
* You must put an object in/on a receptacle after either going to the location of the receptacle or taking an object with you.
* Ensure the first object is placed before proceeding to deposit the second object.
<\Action-Scope>"""
