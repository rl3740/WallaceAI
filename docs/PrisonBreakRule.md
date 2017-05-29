
## Name:
Prison Break

## State:
Center room, air room, lava room. zombies room, trash room, food room, money room
Each room have different states, and have over 300+ in total

## Action:
The agent should found a key. After finding the key, the agent should use the key to open the correct door. Once meet the polices, the agent has two choices, one is use tnt to kill polices, the other one is avoiding polices and running. The agent should find food and money, and then find its own way to the exit, and escape.

## Reward: 
1.	Die from falling in the air: -1000
2.	die from falling into lava: -2000
3.	open the diamond door to exit: 300
4.	open the iron door: 0
5.	open the stone foor: -30
6.	open the sand door: -30
7.	climb up from the ladder: -5
8.	Caught by zombies: -1000
9.	use tnt to kill zombies: 80
10.	open a planks door: -10
11.	pick up a gold: 100
12.     pick up a cake: 50
13.     pick up a dirt: -100
14.     pick up a redstone: 50
15.     error action such as fail to open a door: -50
	  
