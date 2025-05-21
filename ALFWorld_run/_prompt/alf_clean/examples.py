ALF_Clean_Reasoning_Examples = """You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start
[Propose]:
> Think: To solve the task, I need to first find and take an apple, then go to a sinkbasin and clean it with sinkbasin, then put it in sidetable. First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1, diningtable 1, diningtable 2.
> Next-Action-1: go to fridge 1
> Next-Action-2: go to diningtable 1
> Next-Action-3: go to diningtable 2


You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: To solve the task, I need to first find and take an apple, then heat it with microwave, then put it in fridge. First I need to find an apple. An apple is more likely to appear in fridge (1), diningtable (1), coffeetable (1), drawer (1), cabinet (1-13), garbagecan (1). I can check one by one, starting with fridge 1, diningtable 1, coffeetable 1.
> Action: go to fridge 1
The fridge 1 is closed.
> Action: open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.
[Propose]:
> Think: No apple found in fridge 1, I'll check diningtable 1, diningtable 2, diningtable 3.
> Next-Action-1: go to diningtable 1
> Next-Action-2: go to diningtable 2
> Next-Action-3: go to diningtable 3


You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
> Action: go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1, diningtable 2, diningtable 3.
> Action: go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check diningtable 2, diningtable 3, sidetable 1. 
> Action: go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check diningtable 3, sidetable 1, countertop 1. 
> Action: go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1, countertop 1, sinkbasin 1. 
> Action: go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1, sinkbasin 1, garbagecan 1. 
> Action: go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check sinkbasin 1, garbagecan 1, cabinet 1. 
> Action: go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll to check garbagecan 1, cabinet 1, cabinet 2. 
> Action: go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> Think: Now I find an apple (3) on the garbagecan (1). Next, I need to take it.
> Action: take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.
[Propose]:
> Think: Now that I have the apple 3, the next step is to clean it. To clean the apple, I need to go to the sinkbasin 1 and use it to clean the apple. After cleaning, I will go to sidetable 1 and put the apple on it.
> Next-Action-1: go to sinkbasin 1
> Next-Action-2: go to sinkbasin 1
> Next-Action-3: clean apple 3 with sinkbasin 1


You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
> Action: go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1, diningtable 2, diningtable 3.
> Action: go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check diningtable 2, diningtable 3, sidetable 1. 
> Action: go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check diningtable 3, sidetable 1, countertop 1. 
> Action: go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1, countertop 1, sinkbasin 1. 
> Action: go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1, sinkbasin 1, garbagecan 1. 
> Action: go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check sinkbasin 1, garbagecan 1, cabinet 1. 
> Action: go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll to check garbagecan 1, cabinet 1, cabinet 2. 
> Action: go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> Think: Now I find an apple (3) on the garbagecan (1). Next, I need to take it.
> Action: take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.

> Think: Now I get an apple (3). Next, I need to go to sinkbasin (1).
> go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.
[Propose]:
> Think: Now that I am at the sinkbasin 1 with the apple 3, the next step is to clean the apple using the sinkbasin. After cleaning, I will go to the sidetable 1 and place the apple there. The sinkbasin is already accessible, so I can proceed directly to cleaning the apple.
> Next-Action-1: clean apple 3 with sinkbasin 1  
> Next-Action-2: go to sidetable 1  
> Next-Action-3: put apple 3 in/on sidetable 1


You are in the middle of a room. Looking quickly around you, you see a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a cool tomato in microwave.
>Action: Start

> Think: To solve the task, I need to first find and take a tomato, then cool it with the fridge, then put it in the microwave. First, I need to find a tomato. A tomato is more likely to appear in countertop (1-3), cabinet (1-6), drawer (1-3), fridge (1). I can check one by one, starting with countertop 1, countertop 2, and countertop 3.
> Action: go to countertop 1
On the countertop 1, you see a dishsponge 1, and a mug 2.

> Think: No tomato found on countertop 1. I'll check countertop 2, countertop 3, and then the fridge if necessary.
> Action: go to countertop 2
On the countertop 2, you see a butterknife 1, a cellphone 1, a creditcard 1, a knife 1, a lettuce 1, a saltshaker 2, a saltshaker 1, a statue 1, and a tomato 1.

> Think: I have found a tomato (1) on countertop 2. The next step is to take the tomato. Following this, I need to cool it using the fridge, and then place it in the microwave.
> Action: take tomato 1 from countertop 2
You pick up the tomato 1 from the countertop 2.

> Think: Now that I have the tomato 1, the next step is to cool it using the fridge. After cooling the tomato, I will place it in the microwave. To cool the tomato, I need to go to the fridge, place the tomato in it, and then retrieve it once it's cool.
> Action: go to fridge 1
You are located at fridge 1. The fridge 1 is ready, please cool your object directly.

> Think: Now that I am at the fridge 1, the next step is to cool the tomato 1 by placing it in the fridge. Once the tomato is cool, I will take it out and place it in the microwave.
> Action: cool tomato 1 with fridge 1
You cool the tomato 1 using the fridge 1.

> Think: Now that the tomato 1 is cooled, the next step is to place it in the microwave. I need to go to the microwave and put the cooled tomato 1 inside it.
> Action: go to microwave 1
The microwave 1 is closed.
> Action: open microwave 1
You open the microwave 1. The microwave 1 is open. In it, you see a egg 1.

> Think: The microwave 1 currently contains an egg 1. To place the cooled tomato 1 inside, I need to first put tomato 1 in/on somewhere temporarily. After that, I can take egg 1 from microwave 1 and put it in/on somewhere temporarily. Finally, I can put tomato 1 in/on microwave 1.
[Propose]:
> Next-Action-1: go to countertop 1
> Next-Action-2: put tomato 1 on countertop 1
> Next-Action-3: go to microwave 1

You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a countertop 1, a garbagecan 1, a handtowelholder 2, a handtowelholder 1, a sinkbasin 2, a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and a towelholder 1.
Your task is to: clean some cloth and put it in countertop.
>Action: Start

> Think: To complete the task, I first need to find and take some cloth. Cloth is not handtowel, nt towel, not anything else, just cloth. It'll be wrong if I take the handtowel. Cloth is more likely to appear in cabinets (1-4), countertop (1), garbagecan (1), handtowelholder (1-2), and towelholder (1). I can check one by one, starting with cabinet 1, cabinet 2, and cabinet 3.
[Propose]:
> Next-Action-1: go to cabinet 1
> Next-Action-2: go to cabinet 2
> Next-Action-3: go to cabinet 3"""


ALF_Clean_Planning_Examples = """You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
> Action: go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1, diningtable 2, diningtable 3.
> Action: go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check diningtable 2, diningtable 3, sidetable 1. 
> Action: go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check diningtable 3, sidetable 1, countertop 1. 
> Action: go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1, countertop 1, sinkbasin 1. 
> Action: go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1, sinkbasin 1, garbagecan 1. 
> Action: go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check sinkbasin 1, garbagecan 1, cabinet 1. 
> Action: go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll to check garbagecan 1, cabinet 1, cabinet 2. 
> Action: go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> Think: Now I find an apple (3) on the garbagecan (1). Next, I need to take it.
> Action: take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.
[subsequent moves]:
> Think: Now I get an apple (3). Next, I need to go to sinkbasin (1).
> Action: go to sinkbasin 1

> Think: Next I'll clean apple (3) with it.
> Action: clean apple 3 with sinkbasin 1

> Think: Next, I need to go to sidetable 1.
> Action: go to sidetable 1

> Think: Next, I need to put apple 3 in/on sidetable 1.
> Action: put apple 3 in/on sidetable 1


You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean lettuce in diningtable.
> Action: Start

> Think: To solve the task, I need to first find and take a lettuce, then clean it with sinkbasin, then put it in diningtable. First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1, diningtable 1, sinkbasin 1.
> Action: go to fridge 1
The fridge 1 is closed.
> Action: open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.

> Think: No lettuce found in fridge 1, I'll check diningtable 1, sinkbasin 1, stoveburner 1. 
> Action: go to diningtable 1
On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> Think: Now I find a lettuce (1) on the diningtable (1). Next, I need to take it.
> Action: take lettuce 1 from diningtable 1
You pick up the lettuce 1 from the diningtable 1.
[subsequent moves]:
> Think: Now I get a lettuce (1). Next, I need to go to sinkbasin (1).
> Action: go to sinkbasin 1

> Think: Next I'll clean the lettuce (1) with sinkbasin 1.
> Action: clean lettuce 1 with sinkbasin 1

> Think: Now I clean a lettuce (1). Next, I need to go to diningtable 1.
> Action: go to diningtable 1

> Think: Next, I need to put the lettuce (1) in/on diningtable 1.
> Action: put lettuce 1 in/on diningtable 1


You are in the middle of a room. Looking quickly around you, you see a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a cool tomato in microwave.
>Action: Start

> Think: To solve the task, I need to first find and take a tomato, then cool it with the fridge, then put it in the microwave. First, I need to find a tomato. A tomato is more likely to appear in countertop (1-3), cabinet (1-6), drawer (1-3), fridge (1). I can check one by one, starting with countertop 1, countertop 2, and countertop 3.
> Action: go to countertop 1
On the countertop 1, you see a dishsponge 1, and a mug 2.

> Think: No tomato found on countertop 1. I'll check countertop 2, countertop 3, and then the fridge if necessary.
> Action: go to countertop 2
On the countertop 2, you see a butterknife 1, a cellphone 1, a creditcard 1, a knife 1, a lettuce 1, a saltshaker 2, a saltshaker 1, a statue 1, and a tomato 1.

> Think: I have found a tomato (1) on countertop 2. The next step is to take the tomato. Following this, I need to cool it using the fridge, and then place it in the microwave.
> Action: take tomato 1 from countertop 2
You pick up the tomato 1 from the countertop 2.

> Think: Now that I have the tomato 1, the next step is to cool it using the fridge. After cooling the tomato, I will place it in the microwave. To cool the tomato, I need to go to the fridge, place the tomato in it, and then retrieve it once it's cool.
> Action: go to fridge 1
You are located at fridge 1. The fridge 1 is ready, please cool your object directly.

> Think: Now that I am at the fridge 1, the next step is to cool the tomato 1 by placing it in the fridge. Once the tomato is cool, I will take it out and place it in the microwave.
> Action: cool tomato 1 with fridge 1
You cool the tomato 1 using the fridge 1.

> Think: Now that the tomato 1 is cooled, the next step is to place it in the microwave. I need to go to the microwave and put the cooled tomato 1 inside it.
> Action: go to microwave 1
The microwave 1 is closed.
> Action: open microwave 1
You open the microwave 1. The microwave 1 is open. In it, you see a egg 1.
[subsequent moves]:
> Think: The microwave 1 currently contains an egg 1. To place the cooled tomato 1 inside, I need to first put tomato 1 in/on countertop 1 temporarily. After that, I can take egg 1 from microwave 1 and put it in/on countertop 1. Finally, I can put tomato 1 in/on microwave 1.
> Action: go to countertop 1

> Think: Now I am at countertop 1, I can put tomato 1 on countertop 1 temporarily, then I can go to microwave 1 and take egg 1 from microwave 1 and put it in/on countertop 1.
> Action: put tomato 1 on countertop 1

Think: Now I put tomato 1 on countertop 1 temporarily, I can go to microwave 1 and take egg 1 from microwave 1 and put it in/on countertop 1. After that I can go back to countertop 1 to take tomato 1 and put it in/on microwave 1.
> Action: go to microwave 1

> Think: Now I am microwave 1, I can take egg 1 from microwave 1 and put it in/on countertop 1, then I can take tomato 1 from countertop 1 and go to microwave 1 to put it in/on microwave 1.
> Action: take egg 1 from microwave 1

> Think: Now I take egg 1 from microwave 1, then I should put it in/on countertop 1. After that I can take tomato 1 from countertop 1 and go to microwave 1 to put it in/on microwave 1.
> Action: go to countertop 1

> Think: Now I am at countertop 1, I can put egg 1 on countertop 1, then I can take tomato 1 from countertop 1 and go to microwave 1 to put it in/on microwave 1.
> Action: put egg 1 on countertop 1

> Think: Now I can take tomato 1 from countertop 1 and go to microwave 1 to put it in/on microwave 1.
> Action: take tomato 1 from countertop 1

> Think: Now the next step is to place it in the microwave. I need to go to the microwave and put the cooled tomato 1 inside it.
> Action: go to microwave 1

> Think: I arrive drawer 1, I need to put tomato 1 in/on microwave 1.
> Action: put tomato 1 in/on microwave 1"""


ALF_Clean_P_Scoring_Examples = """You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
> Action: go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1, diningtable 2, diningtable 3.
> Action: go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check diningtable 2, diningtable 3, sidetable 1. 
> Action: go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check diningtable 3, sidetable 1, countertop 1. 
> Action: go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1, countertop 1, sinkbasin 1. 
> Action: go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1, sinkbasin 1, garbagecan 1. 
> Action: go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check sinkbasin 1, garbagecan 1, cabinet 1. 
> Action: go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll to check garbagecan 1, cabinet 1, cabinet 2. 
> Action: go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> Think: Now I find an apple (3) on the garbagecan (1). Next, I need to take it.
> Action: take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.
[subsequent moves]:
> Think: Now I get an apple (3). Next, I need to go to sinkbasin (1).
> Action: go to sinkbasin 1

> Think: Next I'll clean apple (3) with it.
> Action: clean apple 3 with sinkbasin 1

> Think: Next, I need to go to sidetable 1.
> Action: go to sidetable 1

> Think: Next, I need to put apple 3 in/on sidetable 1.
> Action: put apple 3 in/on sidetable 1

[reasoning]: The subsequent moves are feasible and align with the task requirements. The robot successfully finds the apple in the garbage can, takes it, cleans it using the sink basin, and then places it on the sidetable. Each step follows the transition rules and the task is completed effectively. Therefore, the action path is fully reliable, warranting a score of 10.

[score]: 10


You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean lettuce in diningtable.
> Action: Start

> Think: To solve the task, I need to first find and take a lettuce, then clean it with sinkbasin, then put it in diningtable. First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1, diningtable 1, sinkbasin 1.
> Action: go to fridge 1
The fridge 1 is closed.
> Action: open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.

> Think: No lettuce found in fridge 1, I'll check diningtable 1, sinkbasin 1, stoveburner 1. 
> Action: go to diningtable 1
On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> Think: Now I find a lettuce (1) on the diningtable (1). Next, I need to take it.
> Action: take lettuce 1 from diningtable 1
You pick up the lettuce 1 from the diningtable 1.
[subsequent moves]:
> Think: Now I get a lettuce (1). Next, I need to go to sinkbasin (1).
> Action: go to sinkbasin 1

> Think: Next I'll clean the lettuce (1) with sinkbasin 1.
> Action: clean lettuce 1 with sinkbasin 1

> Think: Now I clean a lettuce (1). Next, I need to go to diningtable 1.
> Action: go to diningtable 1

> Think: Next, I need to put the lettuce (1) in/on diningtable 1.
> Action: put lettuce 1 in/on diningtable 1

[reasoning]: The subsequent moves are feasible and align with the task requirements. The robot successfully finds the lettuce on the dining table, takes it, cleans it using the sink basin, and then places it back on the dining table. Each step follows the transition rules, and the task is completed effectively. Therefore, the action path is fully reliable, warranting a score of 10.

[score]: 10"""


ALF_Clean_H_Scoring_Examples = """You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: To solve the task, I need to first find and take an apple, then go to a sinkbasin and clean it with sinkbasin, then put it in sidetable. First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1, diningtable 1, diningtable 2.
[next steps]:
> Next-Action-1: go to fridge 1  
[reasoning]: The fridge is a common location where apples might be stored. Checking the fridge first is a logical step to find an apple, which is necessary to proceed with the task. This action directly contributes to the task by initiating the search for the apple.  
[score]: 8  

> Next-Action-2: go to diningtable 1  
[reasoning]: Dining tables are also likely places where apples might be placed, especially if they are being prepared or consumed. Checking diningtable 1 is a reasonable next step if the fridge does not yield an apple. This action is necessary to locate the apple.  
[score]: 7  

> Next-Action-3: go to diningtable 2  
[reasoning]: Similar to diningtable 1, diningtable 2 is another potential location for an apple. However, since diningtable 1 is closer in the sequence and equally likely to have an apple, this action is slightly less prioritized. It is still necessary but less urgent compared to the first two actions.  
[score]: 6


You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet 7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean lettuce in diningtable.
> Action: Start

> Think: To solve the task, I need to first find and take a lettuce, then clean it with sinkbasin, then put it in diningtable. First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1, diningtable 1, sinkbasin 1.
> Action: go to fridge 1
The fridge 1 is closed.
> Action: open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.

> Think: No lettuce found in fridge 1, I'll check diningtable 1, sinkbasin 1, stoveburner 1. 
> Action: go to diningtable 1
On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> Think: Now I find a lettuce (1) on the diningtable (1). Next, I need to take it.
> Action: take lettuce 1 from diningtable 1
You pick up the lettuce 1 from the diningtable 1.

> Think: Now I get a lettuce (1). Next, I need to go to sinkbasin (1).
> go to sinkbasin 1
On the sinkbasin 1, you see a apple 2, a ladle 2, a spoon 1, and a tomato 3.

> Think: Next I'll clean the lettuce (1) with sinkbasin 1.
> clean lettuce 1 with sinkbasin 1
You clean the lettuce 1 using the sinkbasin 1.

> Think: Now I clean a lettuce (1). Next, I need to go to diningtable 1.
[next steps]:
> Next-Action-1: go to diningtable 1
[reasoning]: The robot needs to go to the diningtable 1 to place the clean lettuce there. This is a necessary step because the task requires the lettuce to be placed on the diningtable. However, since the robot is already at the sinkbasin 1, it must first move to the diningtable 1 before it can place the lettuce. This action is essential for completing the task.
[score]: 10

> Next-Action-2: go to diningtable 1
[reasoning]: This action is identical to Next-Action-1 and serves the same purpose. It is necessary for the robot to go to the diningtable 1 to place the clean lettuce. However, since it is a duplicate of the first action, it does not provide any additional value.
[score]: 0

> Next-Action-3: put lettuce 1 in/on diningtable 1  
[reasoning]: Placing the lettuce on the diningtable is the final step of the task. However, this action is currently unfeasible because the robot is not yet at the diningtable. According to the transition rules, the robot must first go to the diningtable before it can place the lettuce there. This action is necessary but cannot be performed until the robot reaches the diningtable.
[score]: 0


You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 1, a diningtable 3, a diningtable 2, a diningtable 1, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a sidetable 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: clean some apple and put it in sidetable.
> Action: Start

> Think: First I need to find an apple. An apple is more likely to appear in fridges (1), diningtable (1-3), sidetable (1), countertop (1), sinkbasin (1), garbagecan (1). I can check one by one, starting with fridge 1.
> Action: go to fridge 1
The fridge 1 is closed.
> open fridge 1
You open the fridge 1. The fridge 1 is open. In it, you see a lettuce 2, a mug 2, a potato 2, and a tomato 1.

> Think: No apple found in fridge 1, I'll check diningtable 1, diningtable 2, diningtable 3.
> Action: go to diningtable 1
On the diningtable 1, you see nothing.

> Think: No apple found on diningtable 1, I'll check diningtable 2, diningtable 3, sidetable 1. 
> Action: go to diningtable 2
On the diningtable 2, you see a pineapple 1.

> Think: No apple found on diningtable 2, I'll check diningtable 3, sidetable 1, countertop 1. 
> Action: go to diningtable 3
On the diningtable 3, you see a bowl 2, a bowl 1, a bread 2, and a bread 1.

> Think: No apple found on diningtable 3, I'll check sidetable 1, countertop 1, sinkbasin 1. 
> Action: go to sidetable 1
On the sidetable 1, you see a cup 1, a lettuce 1, a peppershaker 3, a potato 1, and a saltshaker 1.

> Think: No apple found on sidetable 1, I'll check countertop 1, sinkbasin 1, garbagecan 1. 
> Action: go to countertop 1
On the countertop 1, you see a butterknife 1, a dishsponge 1, and a soapbottle 1.

> Think: No apple found on countertop 1, I'll check sinkbasin 1, garbagecan 1, cabinet 1. 
> Action: go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: No apple found on sinkbasin 1, I'll to check garbagecan 1, cabinet 1, cabinet 2. 
> Action: go to garbagecan 1
On the garbagecan 1, you see a apple 3, and a egg 3.

> Think: Now I find an apple (3) on the garbagecan (1). Next, I need to take it.
> Action: take apple 3 from garbagecan 1
You pick up the apple 3 from the garbagecan 1.

> Think: Now I get an apple (3). Next, I need to go to sinkbasin (1).
> go to sinkbasin 1
On the sinkbasin 1, you see a cup 2, a egg 1, a mug 1, and a potato 3.

> Think: Now that I am at the sinkbasin 1 with the apple 3, the next step is to clean the apple using the sinkbasin. After cleaning, I will go to the sidetable 1 and place the apple there. The sinkbasin is already accessible, so I can proceed directly to cleaning the apple.
[next steps]:
> Next-Action-1: clean apple 3 with sinkbasin 1  
[reasoning]: Cleaning the apple is a necessary step in the task, as the goal is to place a clean apple on the sidetable. Since the robot is already at the sinkbasin 1 and holding the apple, this action is both feasible and essential for progressing toward the task's completion.  
[score]: 10

> Next-Action-2: go to sidetable 1  
[reasoning]: Premature, as the apple must be cleaned first. 
[score]: 0

> Next-Action-3: put apple 3 in/on sidetable 1  
[reasoning]: Unfeasible now; requires cleaning and moving to the sidetable first.  
[score]: 0


You are in the middle of a room. Looking quickly around you, you see a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop 2, a countertop 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1, a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a cool tomato in microwave.
>Action: Start

> Think: To solve the task, I need to first find and take a tomato, then cool it with the fridge, then put it in the microwave. First, I need to find a tomato. A tomato is more likely to appear in countertop (1-3), cabinet (1-6), drawer (1-3), fridge (1). I can check one by one, starting with countertop 1, countertop 2, and countertop 3.
> Action: go to countertop 1
On the countertop 1, you see a dishsponge 1, and a mug 2.

> Think: No tomato found on countertop 1. I'll check countertop 2, countertop 3, and then the fridge if necessary.
> Action: go to countertop 2
On the countertop 2, you see a butterknife 1, a cellphone 1, a creditcard 1, a knife 1, a lettuce 1, a saltshaker 2, a saltshaker 1, a statue 1, and a tomato 1.

> Think: I have found a tomato (1) on countertop 2. The next step is to take the tomato. Following this, I need to cool it using the fridge, and then place it in the microwave.
> Action: take tomato 1 from countertop 2
You pick up the tomato 1 from the countertop 2.

> Think: Now that I have the tomato 1, the next step is to cool it using the fridge. After cooling the tomato, I will place it in the microwave. To cool the tomato, I need to go to the fridge, place the tomato in it, and then retrieve it once it's cool.
> Action: go to fridge 1
You are located at fridge 1. The fridge 1 is ready, please cool your object directly.

> Think: Now that I am at the fridge 1, the next step is to cool the tomato 1 by placing it in the fridge. Once the tomato is cool, I will take it out and place it in the microwave.
> Action: cool tomato 1 with fridge 1
You cool the tomato 1 using the fridge 1.

> Think: Now that the tomato 1 is cooled, the next step is to place it in the microwave. I need to go to the microwave and put the cooled tomato 1 inside it.
> Action: go to microwave 1
The microwave 1 is closed.
> Action: open microwave 1
You open the microwave 1. The microwave 1 is open. In it, you see a egg 1.

> Think: The microwave 1 currently contains an egg 1. To place the cooled tomato 1 inside, I need to first put tomato 1 in/on somewhere temporarily. After that, I can put egg 1 from microwave 1 and put it in/on somewhere temporarily. Finally, I can put tomato 1 in/on microwave 1.
[next steps]:
> Next-Action-1: go to countertop 1  
[reasoning]: The robot needs a temporary location to place the tomato 1 while it handles the egg 1 in the microwave. Countertop 1 is a feasible location for temporarily placing the tomato 1. This action is necessary to free up the robot's ability to handle the egg 1 in the microwave.  
[score]: 10  

> Next-Action-2: put tomato 1 on countertop 1  
[reasoning]: After going to countertop 1, the robot must place the tomato 1 there temporarily. This action is necessary to ensure the tomato 1 is safely stored while the robot deals with the egg 1 in the microwave. However, the robot can't put tomato 1 on countertop 1 without going to countertop 1. 
[score]: 5  

> Next-Action-3: take egg 1 from microwave 1  
[reasoning]: The robot can't take egg 1 from microwave 1 with tomato 1 in its hand. This action is absolutely unfeasible.   
[score]: 0


You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a countertop 1, a garbagecan 1, a handtowelholder 2, a handtowelholder 1, a sinkbasin 2, a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and a towelholder 1.
Your task is to: clean some cloth and put it in countertop.
>Action: Start

> Think: To complete the task, I first need to find and take some cloth. Cloth is more likely to appear in cabinets (1-4), countertop (1), garbagecan (1), handtowelholder (1-2), and towelholder (1). I can check one by one, starting with cabinet 1, cabinet 2, and cabinet 3. Cloth is cloth, handtowel is not cloth.
> Action: go to cabinet 1
The cabinet 1 is closed.
> Action: open cabinet 1
You open the cabinet 1. The cabinet 1 is open. In it, you see a cloth 2.
[next steps]:
> Next-Action-1: take cloth 2 from cabinet 1
[reasoning]: The robot has found a cloth (cloth 2) inside the open cabinet 1. Taking the cloth is the immediate next step to proceed with the task of cleaning it and placing it on the countertop. This action is essential as it directly contributes to the task by acquiring the target object. 
[score]: 10  

> Next-Action-2: take cloth 2 from cabinet 1
[reasoning]: This action is identical to Next-Action-1. While taking the cloth is necessary, proposing the same action twice is redundant and does not provide any additional value.
[score]: 0   

> Next-Action-3: go to sinkbasin 1 
[reasoning]: The sinkbasin is where the cloth will be cleaned, but the robot must first take the cloth before moving to the sinkbasin. This action is premature at this stage and does not contribute to the immediate next step of acquiring the cloth.  
[score]: 0


You are in the middle of a room. Looking quickly around you, you see a cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a countertop 1, a garbagecan 1, a handtowelholder 2, a handtowelholder 1, a sinkbasin 2, a sinkbasin 1, a toilet 1, a toiletpaperhanger 1, and a towelholder 1.
Your task is to: clean some cloth and put it in countertop.
>Action: Start

> Think: To solve the task, I need to first find and take a cloth, then clean it using a sinkbasin, and finally put it on the countertop. A cloth is most likely to be found on handtowelholder (1-2), towelholder (1), or possibly in cabinets (1-4). I should check these locations in order.
> Action: go to handtowelholder 1
On the handtowelholder 1, you see a handtowel 1.
[next steps]:
> Next-Action-1: take handtowel 1 from handtowelholder 1
[reasoning]: The robot needs cloth but handtowelholder is not a cloth, I need to check somewhere else. Taking it would be irrelevant to the task and waste time.
[score]: 0  

> Next-Action-2: go to handtowelholder 2
[reasoning]: While handtowelholder 2 may also contain a handtowel rather than a cloth, it is still a potential location worth checking if the robot follows a systematic search pattern. However, since handtowelholder 1 already had a handtowel (not cloth), this action is less likely to succeed.
[score]: 4   

> Next-Action-3: go to towelholder 1 
[reasoning]: A towelholder is far more likely to contain an actual cloth (e.g., a towel) than a handtowelholder. This should be the highest-priority next step because it has the highest chance of fulfilling the task requirement.
[score]: 9"""