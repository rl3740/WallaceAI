def world(seed = "0"):
    '''
    Document: http://microsoft.github.io/malmo/0.21.0/Schemas/Mission.html#ns_xs
    
    decorating methods:
        <DrawCuboid x1, y1, z1, x2, y2, z2, type/>
        <DrawLine x1, y1, z1, x2, y2, z2, type/>
        <DrawBlock x, y, z, type/>
        <DrawSphere x, y, z, radius, type/>
        <DrawItem x, y, z, type/>
        
    '''
    return'''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
    <About>
        <Summary>This is the Wallace AI, it runs faster than HongKong Journalism</Summary>
    </About>
              

              
              
              
    <ServerSection>
        <ServerInitialConditions>
            <Weather>clear</Weather>
            <Time>
                <AllowPassageOfTime>false</AllowPassageOfTime>
            </Time>
        </ServerInitialConditions>
        <ServerHandlers>
            <FlatWorldGenerator generatorString="3;49,17,3,3,2;1;" destroyAfterUse="1"/>
            <DrawingDecorator>
                <DrawSphere x="0" y="10" z="10" radius="5" type="stone"/>
                <DrawCuboid x1 = "0" y1= "10" z1= "0" x2= "21" y2= "15" z2= "21" type="stone"/>
                <DrawCuboid x1 = "1" y1= "11" z1= "1" x2= "20" y2= "15" z2= "20" type="air"/>
                <DrawCuboid x1 = "3" y1= "11" z1= "3" x2= "3" y2= "15" z2= "3" type="redstone_block"/>
            </DrawingDecorator>
            <ServerQuitWhenAnyAgentFinishes/>
        </ServerHandlers>
    </ServerSection>
              
    <AgentSection mode="Survival">
        <Name>Wallace</Name>
        <AgentStart>
            <Placement x="11" y="13" z="11" yaw="0"/>
        </AgentStart>
        <AgentHandlers>
            <ContinuousMovementCommands turnSpeedDegs="180"/>
            <AgentQuitFromTouchingBlockType>
                <Block type="redstone_block"/>
            </AgentQuitFromTouchingBlockType>
            <ObservationFromFullStats/>
            <ObservationFromGrid>
                <Grid name="walalce_sense">
                    <min x="-1" y="0" z="-1"/>
                    <max x="1" y="0" z="1"/>
                </Grid>
            </ObservationFromGrid>                  
        </AgentHandlers>
    </AgentSection>
    </Mission>'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    