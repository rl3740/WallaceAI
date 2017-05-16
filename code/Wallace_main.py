import MalmoPython
import os
import sys
import time
import json
import random
import go_go_wallace
'''
own methods
'''
from wallace_serve_agent import world

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

# Create default Malmo objects:
agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print ('ERROR:',e)
    print (agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print (agent_host.getUsage())
    exit(0)



my_mission = MalmoPython.MissionSpec(world(), True)
my_mission_record = MalmoPython.MissionRecordSpec()
my_mission.requestVideo(800, 500)   # dunno
my_mission.setViewpoint(2)          # dunno

# Attempt to start a mission:

client_pool = MalmoPython.ClientPool() # '''on RL computer'''
client_pool.add( MalmoPython.ClientInfo( "127.0.0.1", 10001 ) ) # '''on RL computer'''
max_retries = 3

for retry in range(max_retries):
    try:
        #agent_host.startMission( my_mission, my_mission_record ) # original agent
        agent_host.startMission( my_mission, client_pool ,my_mission_record, 0, "" )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print ("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print "Waiting for the Wallace to start "
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    sys.stdout.write(".") # for checking state running
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print( "Error:",error.text)

print  "Wallace is running faster then HK journalism"
'''
everything before moving starts here, calculation, etc.

note: trun 1s = 180
'''

'''
everything before moving starts above, calculation, etc.
'''
# Loop until mission ends:
while world_state.is_mission_running:

    go_go_wallace.move_n_blocks(agent_host, True)
    
    sys.stdout.write(".")
    time.sleep(0.1)    
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print ("Error:",error.text)
    """
    agent movement inside here
    """
    
    
    
    msg = world_state.observations[-1].text #the lastest observation
    observations = json.loads(msg)
    grid = observations.get(u'walalce_sense', 0)
    print grid
    print "block ahead?",go_go_wallace.block_ahead(grid)
    if go_go_wallace.block_ahead(grid):
        degree = random.randrange(-100,100)/100.0 * 360
        print "degree: ", degree
        go_go_wallace.turn_degree(agent_host, degree)
        
        
        
        
        
    """
    agent movement inside here
    """

print()
print ("Mission ended")
# Mission has ended.
