Action_Reasoning_Examples = """ <Question>
    What profession does Nicholas Ray and Elia Kazan have in common?
<\Question>
<State>
    [Action-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [Action-1]: Search[Nicholas Ray profession]
    [Observation-1]: Nicholas Ray&#39;s academic interests include architectural history and theory, as well as the links between architectural theory and practice. Degrees obtained. MA, Architecture, University of Cambridge. Diploma in Architecture, University College, London. Awards and prizes"
<\State>
<Proposes>
    [Thought-a]: The initial search result about Nicholas Ray does not mention his profession in a way that is relevant to the question. A more focused search for his primary profession, such as "Nicholas Ray filmmaker," is necessary.
    [Action-a]: Search[Nicholas Ray filmmaker]
    
    [Thought-b]: Similarly, to find the profession that Elia Kazan shares with Nicholas Ray, a search for Elia Kazan's primary profession should be conducted.
    [Action-b]: Search[Elia Kazan profession]

    [Thought-c]: The result from the search appears to provide information about a different Nicholas Ray. A better approach is to retrieve information directly about Nicholas Ray to clarify his profession.
    [Action-c]: Search[Nicholas Ray]
<\Proposes>


<Question>
    Who was once considered the best kick boxer in the world, however he has been involved in a number of controversies relating to his "unsportsmanlike conducts" in the sport and crimes of violence outside of the ring.
<\Question>
<State>
    [Action-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [Action-1]: Search[best kick boxer controversies]
    [Observation-1]: Former professional kickboxer and hugely followed online influencer Andrew Tate is back in the spotlight following his detention in Romania for 30 days at the request of police.
    [Action-2]: Search[Andrew Tate unsportsmanlike conduct]
    [Observation-2]: A court in Romania’s capital has ruled that a trial can start in the case of influencer Andrew Tate, who is charged with human trafficking, rape and forming a criminal gang to sexually exploit women.The Bucharest Tribunal ruled that prosecutors’ case file against Tate met the legal criteria but did
<\State>
<Proposes>
    [Thought-a]: Since the last search provided insight into Andrew Tate's legal troubles, looking up the keyword 'controversy' will help to find specific instances relating to unsportsmanlike conducts and crimes of violence.
    [Action-a]: Lookup[controversy]
    
    [Thought-b]: After identifying controversies relating to unsportsmanlike conduct and crimes of violence, retrieving more information about Andrew Tate's career as a kickboxer will provide context and evidence to support the claim about him being a best kickboxer.
    [Action-b]: Search[Andrew Tate]

    [Thought-c]: With the information gathered about Andrew Tate's controversies and his kickboxing career, formulate a conclusion about who was once considered the best kickboxer while being involved in controversies.
    [Action-c]: Finish[Badr Hari]
<\Proposes>""" 


Complete_ActionPath_Examlpes = """  <Question>
    What profession does Nicholas Ray and Elia Kazan have in common?
<\Question>
<State>
    [ActionPath-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [ActionPath-1]: Start[]->Search[Nicholas Ray profession]
    [Observation-1]: Nicholas Ray&#39;s academic interests include architectural history and theory, as well as the links between architectural theory and practice. Degrees obtained. MA, Architecture, University of Cambridge. Diploma in Architecture, University College, London. Awards and prizes"
<\State>
<Pending-Plan>
    Start[]->Search[Nicholas Ray profession]->Search[Nicholas Ray]
<\Pending-Plan>
<Completed-ActionPath>  
    Start[]->Search[Nicholas Ray profession]->Search[Nicholas Ray]->Search[Elia Kazan]->Finish[director]  
<\Completed-ActionPath>


<Question>
    Who was inducted into the Rock and Roll Hall of Fame, David Lee Roth or Cia Berg?
<\Question>
<State>
    [ActionPath-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [ActionPath-1]: Start[]->Search[Rock and Roll Hall of Fame]
    [Observation-1]: Visit the Hall of Fame floor to explore the Signature Gallery, the New Inductee Exhibit, and the Power of Rock Experience. See artifacts, videos, and performances from legendary artists like Kate Bush, Sheryl Crow, Missy Elliott, and more.
<\State>
<Pending-Plan>
    Start[]->Search[Rock and Roll Hall of Fame]->Search[David Lee Roth]
<\Pending-Plan>
<Completed-ActionPath>
    Start[]->Search[Rock and Roll Hall of Fame]->Search[David Lee Roth]->Finish[David Lee Roth]
<\Completed-ActionPath>"""


P_Score_ActionPaths_Examples = """  <Question>
    What profession does Nicholas Ray and Elia Kazan have in common?
<\Question>
<State>
    [ActionPath-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [ActionPath-1]: Start[]->Search[Nicholas Ray profession]
    [Observation-1]: Nicholas Ray&#39;s academic interests include architectural history and theory, as well as the links between architectural theory and practice. Degrees obtained. MA, Architecture, University of Cambridge. Diploma in Architecture, University College, London. Awards and prizes"
<\State>
<Candidate-ActionPath>
    [a] Start[]->Search[Nicholas Ray profession]->Search[Nicholas Ray filmmaker]->Search[Nicholas Ray]->Search[Elia Kazan]->Finish[filmmaker]

    [b] Start[]->Search[Nicholas Ray profession]->Search[Elia Kazan profession]->Finish[director]

    [c] Start[]->Search[Nicholas Ray profession]->Search[Nicholas Ray]->Search[Elia Kazan]->Finish[director]
<\Candidate-ActionPath>
<Score>
    [a] Start[]->Search[Nicholas Ray profession]->Search[Nicholas Ray filmmaker]->Search[Nicholas Ray]->Search[Elia Kazan]->Finish[filmmaker]
    [Thought]: This path is somewhat redundant because the initial search already provided information about Nicholas Ray's academic background, which is not relevant to the question. Adding a search for "Nicholas Ray filmmaker" is unnecessary since the question is about a common profession, not specific details about his career. Retrieving both Nicholas Ray and Elia Kazan could help, but the path is overly complex and not directly aligned with finding a common profession.
    [Score]: 5

    [b] Start[]->Search[Nicholas Ray profession]->Search[Elia Kazan profession]->Finish[director]
    [Thought]: This path searches directly for the professions of Nicholas Ray and Elia Kazan separately, avoiding redundant actions and promptly concluding the task. However, it does not attempt to verify retrieved information or confirm the commonality explicitly. While efficient, this reliance on potentially incomplete or ambiguous search results slightly reduces reliability.
    [Score]: 8

    [c] Start[]->Search[Nicholas Ray profession]->Search[Nicholas Ray]->Search[Elia Kazan]->Finish[director]
    [Thought]: This action path starts with a broad search for Nicholas Ray’s profession, then retrieves specific information on both Nicholas Ray and Elia Kazan before concluding. By focusing on retrieval rather than repeated searches, it reduces ambiguity and ensures higher-quality, verifiable information about both individuals. The path balances efficiency with reliability, making it a strong candidate for answering the question accurately.
    [Score]: 9
<\Score>


<Question>
    The lead singer and guitarist in the Portland, Oregon rock band consisting of John Gourley, Zach Carothers, Kyle O'Quin, Jason Sechrist and Eric Howk, goes by what alias?
<\Question>
<State>
    [ActionPath-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [ActionPath-1]: Start[]->Search[Portland rock band members]
    [Observation-1]: Across 21 years, the Portland group has become one of metal&#39;s best-reviewed bands anywhere, drawing notice from Decibel to NPR to Stereogum for its progressive sound.
<\State>
<Candidate-ActionPath>
    [a] Start[]->Search[Portland rock band members]->Search[Portland rock band John Gourley Zach Carothers Kyle O'Quin Jason Sechrist Eric Howk]->Search[Portugal. The Man]->Finish[John Gourley]

    [b] Start[]->Search[Portland rock band members]->Search[Portland rock band John Gourley lead singer guitarist alias]->Search[John Gourley]->Finish[Chris Funk]

    [c] Start[]->Search[Portland rock band members]->Search[Portland rock band John Gourley]->Finish[Portugal. The Man]
<\Candidate-ActionPath>
<Score>
    [a] Start[]->Search[Portland rock band members]->Search[Portland rock band John Gourley Zach Carothers Kyle O'Quin Jason Sechrist Eric Howk]->Search[Portugal. The Man]->Finish[John Gourley]
    [Thought]: This path starts with a broad search for Portland rock band members, which is relevant. However, the subsequent search for a specific combination of members is overly specific and may not yield useful results. Retrieving "Portugal. The Man" is incorrect as it is a different band, and concluding with "John Gourley" is also incorrect since the question asks for the alias of the lead singer and guitarist. This path is not aligned with the question and leads to an incorrect answer.
    [Score]: 2

    [b] Start[]->Search[Portland rock band members]->Search[Portland rock band John Gourley lead singer guitarist alias]->Search[John Gourley]->Finish[Chris Funk]
    [Thought]: This path attempts to directly search for the alias of the lead singer and guitarist, which is relevant to the question. However, retrieving "John Gourley" is incorrect as it does not provide the alias. Concluding with "Chris Funk" is also incorrect as it is not the alias of the lead singer and guitarist. This path fails to provide the correct answer despite being somewhat aligned with the question.
    [Score]: 3

    [c] Start[]->Search[Portland rock band members]->Search[Portland rock band John Gourley]->Finish[Portugal. The Man]
    [Thought]: This path starts with a broad search for Portland rock band members, which is relevant. However, retrieving "Portland rock band John Gourley" is incorrect as it does not provide the alias of the lead singer and guitarist. Concluding with "Portugal. The Man" is also incorrect as it is a different band. This path is not aligned with the question and leads to an incorrect answer.
    [Score]: 2
<\Score>"""


H_Score_Actions_Examples = """  <Question>
    The lead singer and guitarist in the Portland, Oregon rock band consisting of John Gourley, Zach Carothers, Kyle O'Quin, Jason Sechrist and Eric Howk, goes by what alias?
<\Question>
<State>
    [Action-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [Action-1]: Search[Portland rock band members]
    [Observation-1]: Across 21 years, the Portland group has become one of metal&#39;s best-reviewed bands anywhere, drawing notice from Decibel to NPR to Stereogum for its progressive sound.
<\State>
<Candidate-Next-Action>
    [a] Search[Portland rock band John Gourley Zach Carothers Kyle O'Quin Jason Sechrist Eric Howk]

    [b] Search[Portland rock band John Gourley lead singer guitarist alias]

    [c] Search[Portland rock band John Gourley]
<\Candidate-Next-Action>
<Score>
    [a] Search[Portland rock band John Gourley Zach Carothers Kyle O'Quin Jason Sechrist Eric Howk]
    [Thought]: This action is somewhat redundant because the previous search already provided information about a Portland rock band, albeit without specific details about the members listed in the question. Searching again for the exact combination of members is overly specific and may not yield additional useful information. It does not directly address the need to find the alias of the lead singer and guitarist.
    [Score]: 4

    [b] Search[Portland rock band John Gourley lead singer guitarist alias]
    [Thought]: This action focuses specifically on the lead singer and guitarist, John Gourley, and seeks his alias directly. It aligns with the question and is highly likely to yield the necessary information quickly. This is the most efficient search action given the current state. 
    [Score]: 9

    [c] Search[Portland rock band John Gourley]
    [Thought]: This action is somewhat relevant but not entirely necessary at this stage. Retrieving information about John Gourley alone may not provide the alias of the lead singer and guitarist, which is the core requirement of the question. It could be useful if the retrieved information includes the alias, but it is not guaranteed.
    [Score]: 6
<\Score>


<Question>
    What profession does Nicholas Ray and Elia Kazan have in common?
<\Question>
<State>
    [Action-0]: Start[]
    [Observation-0]: The planning agent starts thinking.
    [Action-1]: Search[Nicholas Ray profession]
    [Observation-1]: Nicholas Ray&#39;s academic interests include architectural history and theory, as well as the links between architectural theory and practice. Degrees obtained. MA, Architecture, University of Cambridge. Diploma in Architecture, University College, London. Awards and prizes"
<\State>
<Candidate-Next-Action>
    [a] Search[Nicholas Ray filmmaker]

    [b] Search[Elia Kazan profession]

    [c] Search[Nicholas Ray]
<\Candidate-Next-Action>
<Score>
    [a] Search[Nicholas Ray filmmaker]
    [Thought]: This action is somewhat redundant because the previous search already provided information about Nicholas Ray's academic interests and degrees in architecture. Searching specifically for him as a filmmaker does not directly address the need to find a common profession with Elia Kazan. It may provide additional information but is not the most efficient next step.
    [Score]: 4

    [b] Search[Elia Kazan profession]
    [Thought]: This action is entirely necessary and will significantly help the robot gather missing information to answer the question. The current state only provides information about Nicholas Ray's academic background, and searching for Elia Kazan's profession is essential to find a common profession between the two. This is the most efficient search action given the current state.
    [Score]: 10

    [c] Search[Nicholas Ray]
    [Thought]: This action could provide additional details about Nicholas Ray, but it may be redundant given that the previous search already retrieved some biographical information about him. If the information does not relate to his profession as a filmmaker, this action may not help clarify the shared profession with Elia Kazan.
    [Score]: 5
<\Score>"""