---
layout: default
title: Status
---

## Project Summary
After the cafully thinking, we improved our maze to a prinson brek game. We designed several rooms in the map and different rooms have different tasks. The agent should learn how to pick up stuffs, how to master tools and how to escape from the prison. We will set up some zombies and traps in the room. And we will put some tools such that redstones, sticks, food, money and ladder as well. The agent should pick up these tools to escape. For the first version of our Prison Break game, we tried to set up 9 rooms. The agent learn pick up tools and used existing tools open the doors and faces different situations. There are traps, zombies, tools and exit behind the door. 

## Approach


## Evaluation
- Quantitative Evaluation
  - We tried to evaluate the accuracy of our project. In our project, accuracy means the agent should pick up all tools when it meets foods, money, sticks and redstones. And the agent will use redstone open the door when it stands in front of the door. The agent should not try to use sticks ,foods or something else open the door. Thus, we created 3 rooms with door and put some foods, money and redstones on the floor. Once the agent picked up the first thing, it will get 10 points rewards. Thus, the agent kept picking stuffs up. When the agent tried to open the door, the agent used different tools to try. Our agent tried sticks and foods first. After several times, the agent used redstone open a door and get 100 rewards. The agent learn that using redstone open door is correct. Since the agent already learn how to open the door, it will use redstone open the rest of 2 doors.
 
- Qualitative Evaluation
  - So far, we used simple example and error analysis in our project. The thing we did is assuming the agent will acts like we expected before running the program. And we check the results with our expectation. If the results does not satisfied our expection, we fixed the mistake and improved our program. During the process of evaluation, we assumed the agent will use the sticks it picked up to kill the zombie. In our setup environment, there are some rooms locked the zombie. If the agent choosed the zombie room, the agent should kill the zombie and get 200 points. If the agent does not kill the zombie, the agent will die. When we did the evaluation, our agent did not use the sticks kill the zombie and die several times. After 10 times, the agent tried to use his tools kill zombie. But it choose tools ramdomly. After 50 times trial, our agent found the stick and killed zombie successfully. Since the agent already learn how to kill the zombie, it will kill zombie by using sticks later.
