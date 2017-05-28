from __future__ import division
from collections import defaultdict, deque
from timeit import default_timer as timer
import numpy as np
import MalmoPython
import os
import random
import sys
import time
import json
import random
import math
import errno
from wallace_states import *

inventory_limit = 10


class Wallace(object):
    def __init__(self, alpha=0.3, gamma=1, n=1):
        """Constructing an RL agent.

        Args
            alpha:  <float>  learning rate      (default = 0.3)
            gamma:  <float>  value decay rate   (default = 1)
            n:      <int>    number of back steps to update (default = 1)
        """
        self.epsilon = 0.2  # chance of taking a random action instead of the best
        self.q_table = {}
        self.n, self.alpha, self.gamma = n, alpha, gamma
        self.inventory = defaultdict(lambda: 0, {})
        self.num_items_in_inv = 0
        self.current_room = "center_room"

        self.all_item = all_states
        self.item = all_states[self.current_room]

# ------------------------------- Not important -----------------------------------------
    @staticmethod
    def is_solution(reward):
        """If the reward equals to the maximum reward possible returns True, False otherwise. """
        return reward >= 400

    def get_curr_state(self):
        """Creates a unique identifier for a state.

        The state is defined as the items in the agent inventory. Notice that the state has to be sorted -- otherwise
        differnt order in the inventory will be different states.
        """
        return tuple(sorted(self.inventory.items()))

    def clear_inventory(self):
        """Resets the inventory in case of a new attempt to fetch. """
        self.inventory = defaultdict(lambda: 0, {})          #maybe here with {}
        self.num_items_in_inv = 0
        self.current_room = "center_room"

        self.all_item = all_states
        self.item = all_states[self.current_room]

    # @staticmethod
    # def get_obj_locations(agent_host):
    #     """Queries for the object's location in the world.
    #
    #     As a side effect it also returns Wallace's location.
    #     """
    #     nearyby_obs = {}
    #     while True:
    #         world_state = agent_host.getWorldState()
    #         if world_state.number_of_observations_since_last_state > 0:
    #             msg = world_state.observations[-1].text
    #             ob = json.loads(msg)
    #             for ent in  ob['entities']:
    #                 name = ent['name']
    #                 # if name != 'Chester':
    #                 nearyby_obs[name] = (ent['yaw'], ent['x'], ent['z'])
    #
    #             return nearyby_obs

    # def was_item_picked(self, agent_host, item):
    #     """Goes over the inventory observation and check if the item was picked. """
    #     prev_item_count = self.inventory[item]
    #     while True:
    #         world_state = agent_host.getWorldState()
    #         if world_state.number_of_observations_since_last_state > 0:
    #             msg = world_state.observations[-1].text
    #             ob = json.loads(msg)
    #
    #             for i in xrange(9):
    #                 key = 'InventorySlot_%d_item' % i
    #                 if key in ob:
    #                     inv_item = ob[key]
    #                     inv_counts = ob['InventorySlot_%d_size' % i]
    #
    #                     if inv_item == item and inv_counts > prev_item_count:
    #                         return True
    #                 else:
    #                     break
    #
    #         return False

    def teleport(self, agent_host, teleport_x, teleport_z):
        """Directly teleport to a specific position."""
        tp_command = "tp " + str(teleport_x)+ " 15 " + str(teleport_z)
        agent_host.sendCommand(tp_command)
        time.sleep(0.3)
        # good_frame = False
        # start = timer()
        # while not good_frame:
        #     world_state = agent_host.getWorldState()
        #     if not world_state.is_mission_running:
        #         print "Mission ended prematurely - error."
        #         exit(1)
        #     if not good_frame and world_state.number_of_video_frames_since_last_state > 0:
        #         frame_x = world_state.video_frames[-1].xPos
        #         frame_z = world_state.video_frames[-1].zPos
        #         if math.fabs(frame_x - teleport_x) < 0.001 and math.fabs(frame_z - teleport_z) < 0.001:
        #             good_frame = True
        #             end_frame = timer()

    def fetch_item(self, agent_host, item_to_pick):
        """Finds the object in the world and picks it up (by teleporting to it).

        Will not pick up the item if Chester has more than 3 items in his mouth :)
        """
        # if self.num_items_in_inv > inventory_limit:
        #     return
        # # teleport
        # obj_locs = self.get_obj_locations(agent_host)
        # print "object_location: ", obj_locs
        # my_yaw, my_x, my_z = obj_locs['Wallace']
        # obj_yaw, obj_x, obj_z = obj_locs[item_to_pick]
        object_location = item_locations[item_to_pick]
        self.teleport(agent_host, object_location[0], object_location[1])
        time.sleep(0.3)  # Letting the host pick up on the things that were picked up
        # while True:
        #     if self.was_item_picked(agent_host, item_to_pick) or item_to_pick not in obj_locs:
        #         break
        #
        # time.sleep(0.1)  # Letting the host pick up on the things that were picked up

        self.update_inventory(item_to_pick, "succeed")
        self.num_items_in_inv += 1
        #self.update_item(item_to_pick)

# ------------------------------ Still Working -------------------------------------------
    def update_inventory(self, action, result, option = "none"):
        if option != "none":
            self.inventory[option] += 1
            print "(" + action + "," + option + "),",
        else:
            self.inventory[action] += 1
            print "(" + action + "," + result + "),",

    def update_status(self, room):
        self.current_room = room
        self.item = self.all_item[room]
        print self.current_room

    # def update_item(self, item):
    #     print self.item, item
    #     self.item.remove(item)
    #     self.all_item[self.current_room] = self.item

    def send_wallace(self, agent_host, action):
        # if "redstone" not in self.inventory:
        #     self.update_inventory(action, "Fail", "error_action")
        #     return
        if self.current_room == "center_room":
            if action == "sand":
                if action not in self.inventory.keys():
                    self.update_inventory(action, "Succeed")
                    if "tnt" not in self.inventory:
                        self.update_inventory(action, "Fail", "brown_mushroom_block_without_tnt")
                        self.teleport(agent_host, 15, 5)
                        self.update_status("zombies_room")
                        self.end_action(agent_host)
                    else:
                        self.update_inventory(action, "Succeed", "brown_mushroom_block_with_tnt")
                        self.teleport(agent_host, 15, 5)
                        self.update_status("zombies_room")
                else:
                    self.update_inventory(action, "Succeed")
                    self.teleport(agent_host, 15, 5)
                    self.update_status("zombies_room")
            elif action == "stone":
                self.update_inventory(action, "Succeed")
                self.teleport(agent_host, 15, 25)
                self.update_status("food_room")
            elif action == "iron_block":
                self.update_inventory(action, "Succeed")
                self.update_inventory(action, "Fail", "air")
                self.teleport(agent_host, 15, 15) #TODO
                self.update_status("air_room")
                self.end_action(agent_host)
            elif action == "ladder":
                self.update_inventory(action, "Succeed")
                self.update_inventory(action, "Fail", "lava")
                self.teleport(agent_host, 15, 15) #TODO
                self.update_status("lava_room")
                self.end_action(agent_host)
        elif self.current_room == "zombies_room":
            self.update_inventory(action, "Succeed")
            if action == "planks":
                self.teleport(agent_host, 5, 5)
                self.update_status("trash_room")
            elif action == "diamond_block":
                self.teleport(agent_host, 25, 5)
                #self.update_status("safe_room")
                self.end_action(agent_host)
            elif action == "sand":
                self.teleport(agent_host, 15, 15)
                self.update_status("center_room")
        elif self.current_room == "food_room":
            self.update_inventory(action, "Succeed")
            if action == "planks":
                self.teleport(agent_host, 25, 25)
                self.update_status("money_room")
            elif action == "stone":
                self.teleport(agent_host, 15, 15)
                self.update_status("center_room")
            elif action == "diamond_block":
                self.teleport(agent_host, 5, 25)
                #self.update_status("safe_room")
                self.end_action(agent_host)
        elif self.current_room == "trash_room":
            self.update_inventory(action, "Succeed")
            self.teleport(agent_host, 15, 5)
            self.update_status("zombies_room")
        elif self.current_room == "money_room":
            self.update_inventory(action, "Succeed")
            self.teleport(agent_host, 15, 25)
            self.update_status("food_room")

    def end_action(self, agent_host):
        """Calculates the reward points for the current inventory.

        Args
            agent_host: the host object

        Returns
            reward:     <float> current reward from world state
        """
        current_r = 0
        #time.sleep(0.1)

        for item, counts in self.inventory.items():
            current_r += rewards_map[item] * counts

        agent_host.sendCommand('quit')
        #time.sleep(0.25)
        return current_r

    def get_possible_actions(self, agent_host, is_first_action=False):
        """Returns all possible actions that can be done at the current state. """
        action_list = []
        if not is_first_action:
            # Not allowing Chester to come back empty.
            action_list = ['end_action']

        # craft_opt = self.get_crafting_options()
        # if len(craft_opt) > 0:
        #     action_list.extend(['c_%s' % craft_item for craft_item in craft_opt])

        # if self.num_items_in_inv < inventory_limit:
        #     nearby_obj = self.get_obj_locations(agent_host)
        #     if len(nearby_obj) > 1:
        #         action_list.extend([item for item in nearby_obj.keys() if item != 'Wallace'])

        result = [i for i in self.item if i not in self.inventory.keys()]
        action_list.extend(result)
        return action_list

    def choose_action(self, curr_state, possible_actions, eps):
        """Chooses an action according to eps-greedy policy. """
        if curr_state not in self.q_table:
            self.q_table[curr_state] = {}
        for action in possible_actions:
            if action not in self.q_table[curr_state]:
                self.q_table[curr_state][action] = 0

        rnd = random.random()
        if rnd < eps:
            a = random.randint(0, len(possible_actions) - 1)
            return possible_actions[a]
        else:
            temp = self.q_table[curr_state].items()
            max_q = temp[0]
            for i in range(1, len(temp)):
                if temp[i][1] > max_q[1]:
                    max_q = temp[i]
            return max_q[0]

    def act(self, agent_host, action):

        if action == 'end_action':
            return self.end_action(agent_host)
        elif action in teleporting_list:
            self.send_wallace(agent_host, action)
        elif action in picking_list:
            self.fetch_item(agent_host, action)

        return 0

    def update_q_table(self, tau, S, A, R, T):
        """Performs relevant updates for state tau.

        Args
            tau: <int>  state index to update
            S:   <dequqe>   states queue
            A:   <dequqe>   actions queue
            R:   <dequqe>   rewards queue
            T:   <int>      terminating state index
        """
        curr_s, curr_a, curr_r = S.popleft(), A.popleft(), R.popleft()
        G = sum([self.gamma ** i * R[i] for i in range(len(S))])
        if tau + self.n < T:
            G += self.gamma ** self.n * self.q_table[S[-1]][A[-1]]

        old_q = self.q_table[curr_s][curr_a]
        self.q_table[curr_s][curr_a] = old_q + self.alpha * (G - old_q)

    def best_policy(self, agent_host):
        """Reconstructs the best action list according to the greedy policy. """
        self.clear_inventory()
        policy = []
        current_r = 0
        is_first_action = True
        next_a = ""
        while next_a != "end_action":
            curr_state = self.get_curr_state()
            possible_actions = self.get_possible_actions(agent_host, is_first_action)
            next_a = self.choose_action(curr_state, possible_actions, 0)
            policy.append(next_a)
            is_first_action = False
            current_r = self.act(agent_host, next_a)
        print ' with reward %.1f' % (current_r)
        return self.is_solution(current_r)
        # print 'Best policy so far is %s with reward %.1f' % (policy, current_r)

    def run(self, agent_host):
        """Learns the process to compile the best gift for dad. """
        S, A, R = deque(), deque(), deque()
        present_reward = 0
        time.sleep(1)
        done_update = False
        while not done_update:
            s0 = self.get_curr_state()
            possible_actions = self.get_possible_actions(agent_host, True)
            a0 = self.choose_action(s0, possible_actions, self.epsilon)
            S.append(s0)
            A.append(a0)
            R.append(0)

            T = sys.maxint
            for t in xrange(sys.maxint):
                time.sleep(0.1)
                if t < T:
                    current_r = self.act(agent_host, A[-1])
                    R.append(current_r)

                    if A[-1] == "end_action":
                        # Terminating state
                        T = t + 1
                        S.append('Term State')
                        present_reward = current_r
                        print "Reward:", present_reward
                    else:
                        s = self.get_curr_state()
                        S.append(s)
                        possible_actions = self.get_possible_actions(agent_host)
                        next_a = self.choose_action(s, possible_actions, self.epsilon)
                        A.append(next_a)

                tau = t - self.n + 1
                if tau >= 0:
                    self.update_q_table(tau, S, A, R, T)

                if tau == T - 1:
                    while len(S) > 1:
                        tau += 1
                        self.update_q_table(tau, S, A, R, T)
                    done_update = True
                    break
