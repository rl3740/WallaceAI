#safe room top left and bottom right
#---------------------------------------------------------------------------------------
#                            |                           |                             |
#            safe room       |         air room          |           money_room        |
#                            |                           |                             |
#---------------------------------------------------------------------------------------
#                            |                           |                             |
#         zombies room       |         center room       |           food_room         |
#                            |                           |                             |
#---------------------------------------------------------------------------------------
#                            |                           |                             |
#            trash room      |         fire room         |           safe_room         |
#                            |                           |                             |
#---------------------------------------------------------------------------------------


# Any time there is a possibility that the agent is sent to a mysterious room which is
# a place that is out of nowhere, we use this special case to test the Q-learning algorithm,
# and see whether it works


# start here
center_room = ["ladder", "redstone", "sand", "stone", "iron_block", "tnt", "tnt", "tnt"]

# This room can lead to safe room or a zombies room
zombies_room = ["brown_mushroom_block", "sand", "diamond_block", "planks"]

# this room can lead to safe room or money room
food_room = ["cake", "stone", "diamond_block", "planks", "cake", "cake"]

# must die
air_room = ["air"]

# must die
lava_room = ["lava"]

# money has positive reward
money_room = ["gold_block", "planks", "gold_block", "gold_block"]

# trash has negative reward
trash_room = ["dirt", "planks", "dirt", "dirt"]

mysterious_room = ["air", "lava", "brown_mushroom_block"]

all_states = {"center_room": center_room, "air_room": air_room, "lava_room": lava_room,
              "zombies_room": zombies_room,
              "trash_room": trash_room, "food_room": food_room, "money_room": money_room,
              "mysterious_room": mysterious_room
              }

rewards_map = {"air": -1000, "lava": -2000, "diamond_block": 300, "iron_block": 0, "stone": -30,
               "sand": -30, "ladder": -5, "planks": -10,
               "gold_block": 100, "cake": 50, "dirt": -100, "tnt": -60,
               "brown_mushroom_block_with_tnt": 80,
               "brown_mushroom_block_without_tnt": -1000, "redstone": 50,
               "more_gold_block": -50, "more_cake": -25, "more_tnt": -30, "more_dirt": -50,
               "error_action": -50
               }

teleporting_list = ["ladder", "planks", "sand", "stone", "diamond_block", "iron_block"]
picking_list = ["gold_block", "cake", "dirt", "tnt", "redstone"]

item_locations = {"gold_block": (26, 26), "cake": (16, 26), "dirt": (2, 2), "tnt": (16, 16),
                  "redstone": (13, 13)}
