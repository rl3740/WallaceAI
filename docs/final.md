---
layout: default
title: Final Report
---
## Video

[![Legend of Wallace](https://img.youtube.com/vi/XtD2K157d3Q/0.jpg)](https://www.youtube.com/watch?v=XtD2K157d3Q)

## Project Summary

Just like our subtitle indicating, the goal of our project is to ensure that the agent, Wallace, is able to find the best and fastest way out of the prison. As we know, prisoner usually failed to escape for many times before they finally succeed. Our project implements the reinforcement learning strategy, which make the agent do the same thing as in reality. 

In order to reach the final goal, Wallace will keep trying to escape until he finds the best choice to get out. Even though, he is likely to fail so many times before he can actually make it, he will learn something during the process of trying and failing with a multi-layer Q-learning algorithm that we create for him.

Moreover, we have updated a lot since the status report. Last time, our goal is merely focusing on the overall performance of the system. For instance, whether the rewards of those states are feasible or not, and whether it is possible to find out the ideal solution that we expected. However, right now we are focusing on whether it can be better, and whether it can handle various kinds of crucial situation that we had made to test it. In a machine learning expert’s perspective, the AI need to have low rate of error in both training and testing tasks. I will explain it in more details in the following few sections of the report.

## Approach

#### Some Basic Information of Our project (in case you did not read anything before)

This is the map of our Minecraft world, which is also the prison where the agent, Wallace, was locked.

<img src="img/room_map.jpg" width="40%">

And in the game, it looks like this:

<img src="img/overview.png" width="40%">

The main idea of this design is to 

- ### States
  Our map has 9 rooms which are distributed in a 3 * 3 matrix.
  First row from left to right: Safe room, Hell, Money room.
  Second row from left to right: Zombies room, Wallace room, Foods room.
  Third row from left to right: Trash room, Lava room, Safe room.
  Different rooms hold different states.
  
  - Wallace room: Wallace room locates at the center of the map. Agent Wallace starts his journey from this room. In this room, we put TNT, ladder and redstones on the floor. Wallace should pick up all tools in this room.
  - Foods room: There should be a cake in this room. Agent Wallace need to eat this cake to fill up its stamina.
  - Money room: There is a gold in Money room. Agent Wallace can pick up and take the gold to escape map.
  - Safe room * 2: This rooms are safe zone and next to the exit. Agent Wallace can escape the prison from this room.
  - lava room: Agent Wallace should use the ladder that picked up in the Wallace room go over the lava safely. Otherwise, lava will kill the agent Wallace. 
  - Hell: Agent Wallace should use the ladder that picked up in the Wallace room go over the hell safely. Otherwise, Wallace will fell into the hell.
  - Zombies room: Agent Wallace should use TNT to kill zombies in this room.
  - Trash room: This room is a trap. We set up trash room to allure agent Wallace. All the stuffs in this room is useless. Once agent Wallace picks it up in this room, Wallace will lose points.
  
- ### Game Rules
  Main purpose: Our agent Wallace picks up different tools and enter different rooms to escape the prison.
  Rewards:
  - Redstone: Pick up -- +10, Use and open the door -- +20;
  - TNT: Pick up -- +10, Kill zombie -- +200;
  - Ladder: Pick up -- +10, Use to avoid lava and hell safely -- +200;
  - Cake: Pick up -- +10, eat -- +100;
  - Trash: Pick up -- -10;
  - Gold: Pick up -- +10.

## Evaluation
- Quantitative Evaluation
  - 
 
- Qualitative Evaluation
  - 

## References

- The information of Mike Wallace: https://en.wikipedia.org/wiki/Mike_Wallace

- More information of Mike Wallace: http://baike.baidu.com/item/%E8%BF%88%E5%85%8B%C2%B7%E5%8D%8E%E8%8E%B1%E5%A3%AB?fromtitle=Mike+Wallace&fromid=11258487

- Police arresting image: https://www.selectsr22insurance.com/10-facts-about-getting-arrested-for-dui/

- Reinforcement Learning wikipedia page: https://en.wikipedia.org/wiki/Reinforcement_learning

- MDP wikipedia page: https://en.wikipedia.org/wiki/Markov_decision_process

- Q-learning wikipedia page: https://en.wikipedia.org/wiki/Q-learning

- Article about Q-learning: http://artint.info/html/ArtInt_265.html

- Piazza: https://piazza.com/class/j0lnpjwfdj4150

- stackoverflow: https://stackoverflow.com/

- Q-learning tutorial: http://mnemstudio.org/path-finding-q-learning-tutorial.htm

- MDP examples: https://isites.harvard.edu/fs/docs/icb.topic540049.files/cs181_lec03_handout.pdf

- Minecraft Prison Break example: http://www.minecraftforum.net/forums/mapping-and-modding/maps/1515166-prison-break-minecraft-adventure-map

- Reinforcement learning q-learning explanation: https://studywolf.wordpress.com/2012/11/25/reinforcement-learning-q-learning-and-exploration/

- Reinforcement learning code example: https://github.com/tflearn/tflearn/blob/master/examples/reinforcement_learning/atari_1step_qlearning.py

- Malmo tutorial: https://github.com/Microsoft/malmo

- Minecraft Wiki: http://minecraft.gamepedia.com/Minecraft_Wiki and http://www.minecraft101.net/index.html

- Introduction of MDP and reinforcement learning: https://www.cs.cmu.edu/~epxing/Class/10701-08s/Lecture/lecture27-RL.pdf
