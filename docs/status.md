---
layout: default
title: Status
---

<div><iframe width="1280" height="720" src="https://www.youtube.com/embed/XtD2K157d3Q" frameborder="0" allowfullscreen></iframe></div>

## Project Summary
After some intense discussions, we finally decided to change our maze into a Prison_Break game or you can also call it a Room_Escape Game. We have designed a huge cube which is able to fit nine rooms in the map. Furthermore, every room is different, and they all contain either something to help the agent, Wallace to escape or prevent him from living. The agent should learn how to pick up stuffs, how to master tools, and find out the best way to escape from the prison. We will set up some zombies and traps in the room. And we will put some tools such that redstones, tnt, food, money, and ladder as well. The agent should pick up these tools to escape. For the first version of our Prison Break game, we tried to set up 9 rooms. The agent learn pick up tools and used existing tools open the doors and faces different situations. There are traps, zombies, tools and exit behind the door. 

## Approach
Basically, we use reinenforcement learning to approach the goal. Since, the states are not that many, and q-learning is the one that we use. Unlike the q-learning in homework two, we did a lot of updates from that. For example, we had adjusted them more properly fitted to our program.

## Evaluation
- Quantitative Evaluation
  - We tried to evaluate the accuracy of our project. In our project, accuracy means the agent should pick up all useful tools when it meets foods, money, tnt, and redstones. Moreover, the agent will use redstone open the door when it stands in front of the door. The agent should not try to use sticks ,foods or something else open the door. Thus, we created 3 rooms with door and put some foods, money and redstones on the floor. Once the agent picked up the first thing, it will get some points rewards. Thus, the agent kept picking stuffs up. When the agent tried to open the door, the agent used different tools to try. Our agent tried sticks and foods first. After several times, the agent used redstone open a door and get 100 rewards. The agent learn that using redstone open door is correct. Since the agent already learn how to open the door, it will use redstone open the rest of 2 doors.
 
- Qualitative Evaluation
  - So far, we used simple example and error analysis in our project. The thing we did is assuming the agent will acts like we expected before running the program. And we check the results with our expectation. If the results do not satisfied our expection, we fixed the mistake and improved our program. During the process of evaluation, we assumed that the agent will use the tnt it picked up to kill the zombie. In our setup environment, there are a room that are filled with zombies. If the agent choose the zombie room, the agent should kill the zombie and get 80 points. If the agent does not have the tool to kill the zombies, the agent will die. When we did the evaluation, our agent did not have nothing at all and die at first. After around 10 times, the agent tried to use his tools kill zombies.

## Remaining Goals and Challenges
We just finished the map setup and basic q-learning algorithm. So far, we only have nine rooms, and some simple tool without crafting. In next 2 to 3 weeks, we will focused on add more states and rooms on our map. And we will try to change our zombie from static to dynamic.
