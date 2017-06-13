---
layout: default
title: Final Report
---

[![Legend of Wallace](https://img.youtube.com/vi/XtD2K157d3Q/0.jpg)](https://www.youtube.com/watch?v=XtD2K157d3Q)

## Project Summary

Just like our subtitle indicating, the goal of our project is to ensure that the agent, Wallace, is able to find the best and fastest way out of the prison. As we know, prisoner usually failed to escape for many times before they finally succeed. Our project implements the reinforcement learning strategy, which make the agent do the same thing as in reality. 

In order to reach the final goal, Wallace will keep trying to escape until he finds the best choice to get out. Even though, he is likely to fail so many times before he can actually make it, he will learn something during the process of trying and failing with a multi-layer Q-learning algorithm that we create for him.

- ## States
  Our map has 9 rooms which are distributed in a 3 * 3 matrix.
  First row from left to right: Safe room, Hell, Money room.
  Second row from left to right: Zombies room, Wallace room, Foods room.
  Third row from left to right: Trash room, Lava room, Safe room.
  Different rooms hold different states.
  
  - Wallace room: Wallace room locates at the center of the map. Agent Wallace should start his journey from this room. 
  - Foods room: Agent Wallace gets these foods fill up its stamina to escape map.
  - Money room: Agent Wallace gets these money to escape map.
  - Safe room * 2: This rooms are safe zone, agent can escape the whole map from this room.
  - lava room: Lava will kill the agent Wallace
  - Hell: Wallace will fell into the hell.
  - Zombies room: Agent Wallace should use TNT to kill zombies.
  - Trash room: All the stuffs in this room is useless. Once agent Wallace picks it up, Wallace will lose points.


## Approach

<img src="img/wallace_arrest.png" width="35%">

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

- 
