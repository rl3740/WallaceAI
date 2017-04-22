---
layout: default
title:  Proposal
---

## Summary of the Project

The idea of our project is creating and solving some simple smart mazes, which Navigator and some smart tools collecting AI will be involved. The input will be player’s command. The character will follow commands to complete task and explore a complete maze, and the output will be the character reaching the destination in small amount of time. During this process, the character will be collecting some tools in order to help him arrive the destination. Moreover, the smart navigator will guide him to where he supposes to be. For example, the character will learn the best way from home to everywhere.

## AI/ML Algorithms

We will be using some graph algorithms like, Dijktra's Algorithm, Prim-Dijktra-Jarnik Algorithm, and dynamic programming for finding the minimum spanning tree. For the ML alogrithm, nerual network, random froest, decision tree will be applied.

## Evaluation Plan

Quantitative evaluation: 
Numeric metrics: We will calculate the ROC curve and AUC value for our data. The AUC value becomes larger means the performance of our data becomes better. In addition, we should check the accuracy of our algorithm. We need to check whether the start block and end block correct. The test sets will help us to check the accuracy of our project as well. 
Baselines: Our algorithm should find the destination and generate the shortest path correctly and quickly. 

Qualitative evaluation:
Simple example cases: Our idea should work on resolving a maze and finding the best way to the end of the maze. The output will be the length of the shortest path and the rewards for the character.
Error Analysis and Introspection: If the character meet the fire or die in the maze, which means our algorithm has errors. We should to check our algorithm again and again. In addition, we should use the mean squared error to test the performance of our data.
Best example: If the player give a command like “find the nearest tree” or “find a sheep near the house,” our navigator should find and locate the “tree” or the “sheep” correctly and give the character a best way to the “tree” or the “sheep.”


## Appointment with the Instructor

Our meeting time is: 03:30pm - Thursday, April 27, 2017  
The meeting place is: DBH 4204
