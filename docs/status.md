---
layout: default
title: Status
---

<div><iframe width="1280" height="720" src="https://www.youtube.com/embed/XtD2K157d3Q" frameborder="0" allowfullscreen></iframe></div>

## Project Summary
After some intense discussions, we finally decided to change our maze into a Prison_Break game or you can also call it a Room_Escape Game. We have designed a huge cube which is able to fit nine rooms in the map. Furthermore, every room is different, and they all contain either something to help the agent, Wallace to escape or prevent him from living. The agent should learn how to pick up stuffs, how to master tools, and find out the best way to escape from the prison. We will set up some zombies and traps in the room. And we will put some tools such that redstones, tnt, food, money, and ladder as well. The agent should pick up these tools to escape. For the first version of our Prison Break game, we tried to set up 9 rooms. The agent learn pick up tools and used existing tools open the doors and faces different situations. There are traps, zombies, tools and exit behind the door. 

## Approach
Basically, we use reinenforcement learning to approach the goal. Since, the states are not that many, and q-learning is the one that we use. Unlike the q-learning in homework two, we did a lot of updates from that. For example, we had adjusted them more properly fitted to our program.

![alt text](http://wx1.sinaimg.cn/mw690/74cf960cgy1fg396x3s5tj20m80chdge.jpg)

Secondly, the MDP is quite clear in the project. From the computer's aspect, the states in this project can be infinite, because the AI can go between the room for infinite times. However, since it's not possible for the program to run, and it's not reasonable in the physical world, so I just marked the reward of changing room to be negative. Therefore, the AI will notice that it's not clever to do that frequently, so that it will not go into this kind of states' trap. Ignoring the rstates, the action is fixed, each action is corresponding to an item, which can also understand as each state has one action. For example, if the agent is in the 

## Evaluation
- Quantitative Evaluation
  - We tried to evaluate the accuracy of our project. In our project, accuracy means the agent should pick up all useful tools when it meets foods, money, tnt, and redstones. Moreover, the agent will use redstone open the door when it stands in front of the door. The agent should not try to use sticks ,foods or something else open the door. Thus, we created a Wallace room with door and put some tnt and redstones on the Wallace room to test our agent. For accuracy test, the agent should pick up tnt and redstones. At the first several trials, the agent did not pick up TNT. When it stand in the zombie room, the agent cannot bomb the zombie and die. And the agent went back and picked other stuffs to try. The agent repeated these actions again and again until it picked up all the useful tools. Thus, the accuracy requires agent to pick up all useful tools. Our second trail is testing the agent can use redstones open the door accurately. When the agent tried to open the door, the agent used different tools to try. Our agent tried TNT and foods first, but those did not work. After several times, the agent used redstone open a door and get 100 rewards. The agent learned that using redstone open the door is correct. Since the agent already learn how to open the door, it will use redstone open the rest of doors.
 
- Qualitative Evaluation
  - So far, we just allowed the agent exit through the money and food room to get full credits. Thus, we only used simple example and error analysis in our project. The thing we did is assuming the agent will acts like we expected before running the program. And we check the results with our expectation. If the results do not satisfied our expection, we fixed the mistake and improved our program. During the process of evaluation, we assumed that the agent will use the tnt it picked up to kill the zombie. In our setup environment, there are a room that are filled with zombies. If the agent choose the zombie room, the agent should kill the zombie and get 80 points. If the agent does not have the tnt to kill the zombies, the agent will die. When we did the evaluation, our agent did not have nothing at all and die at first. After around 10 times, the agent tried to use his tools kill zombies.

## Remaining Goals and Challenges
We just finished the map setup and basic q-learning algorithm. So far, we only have nine rooms, and some simple tool without crafting. In next 2 to 3 weeks, we will focused on add more states and rooms on our map. And we will try to change our zombie from static to dynamic. Our program still needs to improve, so we should allow the agent not only exit through money and food room, but also kill zombies and exit the map to get full credits.
