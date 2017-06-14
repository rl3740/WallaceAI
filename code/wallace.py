import time
from _collections import defaultdict
import json
from math import sqrt

def setYaw(agent, yaw):
    '''
    manually set agent's facing direction
    and the range of yaw is supposed to be 0-360
    '''
    agent.sendCommand("setYaw "+str(yaw))
    
def blink(agent,x,z):
    tp_command = "tp " + str(x)+ " 12 " + str(z)
    agent.sendCommand(tp_command)
    time.sleep(0.5)

def get_status(agent):
    '''
    return sample: {u'name': u'Wallace', u'yaw': 0.0, u'pitch': 0.0, u'y': 11.0, u'x': 11.0, u'z': 11.942340947219773}
    '''
    for i in json.loads(agent.peekWorldState().observations[-1].text).get(u'entities', 0):
        if i[u'name'] == u'Wallace':
            return i
    raise "Where's wallace?" 

    

def turn_degree(agent,degree):
    '''
    degree: input a degrees
    sent command to the agent
    '''
    turn = float(abs(degree))/180*1.0
    if degree >= 0:
        agent.sendCommand("turn 1")
        time.sleep(turn)
    else:
        agent.sendCommand("turn -1")
        time.sleep(turn)
    agent.sendCommand("turn 0")
    
def move_n_blocks(agent,n = 1, d = 'f', speed = 1, c = False):
    '''
    n: number of blocks
    d: direction, [f]orward, [b]ack, [l]eft, [r]ight,
    speed: moving speed
    c: continuous moving, if True, just moving forward
    '''
    agent.sendCommand("move 0")
    if d == 'f':
        agent.sendCommand("move "+str(speed))
        time.sleep(0.5*n)
    elif d == 'l':
        turn_degree(agent,-90)
        agent.sendCommand("move "+str(speed))
        time.sleep(0.5*n)
    elif d == 'r':
        turn_degree(agent,90)
        agent.sendCommand("move "+str(speed))
        time.sleep(0.5*n)
    else:
        agent.sendCommand("move -"+str(speed))
        time.sleep(0.5*n)
    agent.sendCommand("move 0")
    
def block_ahead(obs):
    '''
    this is specific for a 3*3 wallace sense
    obs: list of observation
    return true/false
    '''
    if obs[6] != u'air'  or obs[7] != u'air' or obs[8] != u'air':
        return True
    return False

def wallace_eye(obs):
    '''
    need to pre-set n*n
    this return a dict of what can wallace see
    four dimension deliminator:
    
                  b
                  |
                  |
            c-----+-----a
                  |
                  |
                  d     
    
    '''
    # pre-set n here
    n = sqrt(obs)
    # pre-set n here
    center_index = (int(len(obs)/n/2.0) + 1 + int(len(obs)/n/2.0)*5) - 1
    a = center_index + int(len(obs)/n/2.0)
    b = center_index + int(len(obs)/n/2.0)*5
    c = center_index - int(len(obs)/n/2.0)
    d = center_index - int(len(obs)/n/2.0)*5
    
    
    
    
    for i in range(len(obs)):
            
        if obs[i] != u'air':
            x_dis = 0
            y_dis = 0
        
      
    result = defaultdict()
    return result  

def tour_all_room(agent):
    agent.sendCommand("pitch 0.1")
    time.sleep(1)
    agent.sendCommand("pitch 0")
    
    room_centers = [[15,15],[5,5],[5,15],[5,25],[15,5],[15,25],[25,5],[25,15],[25,25]]
    for i in room_centers:
        print "wallace in room" + str(i)
        blink(agent,i[0],i[1])
        agent.sendCommand("turn 1")
        time.sleep(4)
        agent.sendCommand("turn 0")
        time.sleep(1)
        
        
        
        
    
    


































        
    