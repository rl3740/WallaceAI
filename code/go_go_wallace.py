import time
from math import acos, degrees
from _collections import defaultdict

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
    n = 5
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


































        
    