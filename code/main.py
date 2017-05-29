"""
Wallace is currently in prison. However, he is smart and innocent. Therefore, he needed to find a way out of that prison

Author: Zhenhai Wu, Ran Li, Kunyu Zhang
"""

from wallace_class import *
from wallace_server import *

if __name__ == '__main__':
    random.seed(0)
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately

    my_client_pool = MalmoPython.ClientPool()
    my_client_pool.add(MalmoPython.ClientInfo("127.0.0.1", 10000))

    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse(sys.argv)
    except RuntimeError as e:
        print 'ERROR:', e
        print agent_host.getUsage()
        exit(1)
    if agent_host.receivedArgument("help"):
        print agent_host.getUsage()
        exit(0)

    num_reps = 30000
    n=1
    wallace = Wallace(n=n)
    print "n=",n
    wallace.clear_inventory()

    expID = "Wallace_q_learning"

    for iRepeat in range(num_reps):
        my_mission = MalmoPython.MissionSpec(world("Wallace " + str(iRepeat)), True)
        my_mission_record = MalmoPython.MissionRecordSpec("./save_%s-map%d-rep%d.tgz" % (expID, iRepeat, iRepeat))  # Records nothing by default
        my_mission_record.recordCommands()
        my_mission_record.recordMP4(20, 400000)
        my_mission_record.recordRewards()
        my_mission_record.recordObservations()

        my_mission.requestVideo(1200, 720)
        my_mission.setViewpoint(1)

        max_retries = 3
        for retry in range(max_retries):
            try:
                # Attempt to start the mission:
                agent_host.startMission(my_mission, my_client_pool, my_mission_record, 0, "Wallace")
                break
            except RuntimeError as e:
                if retry == max_retries - 1:
                    print "Error starting mission", e
                    print "Is the game running?"
                    exit(1)
                else:
                    time.sleep(2)

        world_state = agent_host.getWorldState()
        while not world_state.has_mission_begun:
            time.sleep(0.1)
            world_state = agent_host.getWorldState()

        # Every few iteration Wallace will show us the best policy that he learned.
        if (iRepeat + 1) % 5 == 0:
            print (iRepeat+1), 'Showing best policy:',
            found_solution = wallace.best_policy(agent_host)
            if found_solution:
                print 'Found solution'
                print 'Done'
                break
        else:
            print (iRepeat+1), 'Learning Q-Table:',

            wallace.run(agent_host)

        wallace.clear_inventory()
        time.sleep(1)