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
  
  - Wallace room: Wallace room locates at the center of the map. Agent Wallace starts his journey from this room. In this room, we put TNT, ladder and redstones on the floor. Wallace should pick up all tools in this room.
  - Foods room: There should be a cake in this room. Agent Wallace need to eat this cake to fill up its stamina.
  - Money room: There is a gold in Money room. Agent Wallace can pick up and take the gold to escape map.
  - Safe room * 2: This rooms are safe zone and next to the exit. Agent Wallace can escape the prison from this room.
  - lava room: Agent Wallace should use the ladder that picked up in the Wallace room go over the lava safely. Otherwise, lava will kill the agent Wallace. 
  - Hell: Agent Wallace should use the ladder that picked up in the Wallace room go over the hell safely. Otherwise, Wallace will fell into the hell.
  - Zombies room: Agent Wallace should use TNT to kill zombies in this room.
  - Trash room: This room is a trap. We set up trash room to allure agent Wallace. All the stuffs in this room is useless. Once agent Wallace picks it up in this room, Wallace will lose points.
  
- ## Game Rules
  Main purpose: Our agent Wallace picks up different tools and enter different rooms to escape the prison.
  Rewards:
  - Redstone: Pick up -- +10, Use and open the door -- +20;
  - TNT: Pick up -- +10, Kill zombie -- +200;
  - Ladder: Pick up -- +10, Use to avoid lava and hell safely -- +200;
  - Cake: Pick up -- +10, eat -- +100;
  - Trash: Pick up -- -10;
  - Gold: Pick up -- +10.


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
