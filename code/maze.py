# def maze(seed,gp = 0.4 + float(1/20.0), size = 10):
#     return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
#             <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
# 
#               <About>
#                 <Summary>Hello world!</Summary>
#               </About>
# 
#             <ServerSection>
#               <ServerInitialConditions>
#                 <Time>
#                     <StartTime>1000</StartTime>
#                     <AllowPassageOfTime>false</AllowPassageOfTime>
#                 </Time>
#                 <Weather>clear</Weather>
#               </ServerInitialConditions>
#               <ServerHandlers>
#                   <FlatWorldGenerator generatorString="3;1,2,40,1:1;1;village"/>
#                   <DrawingDecorator>
#                     <DrawSphere x="-27" y="70" z="0" radius="30" type="air"/>
#                   </DrawingDecorator>
#                   <MazeDecorator>
#                     <Seed>'''+str(seed)+'''</Seed>
#                     <SizeAndPosition width="''' + str(size) + '''" length="''' + str(size) + '''" height="10" xOrigin="-32" yOrigin="69" zOrigin="-5"/>
#                     <StartBlock type="emerald_block" fixedToEdge="true"/>
#                     <EndBlock type="redstone_block" fixedToEdge="true"/>
#                     <PathBlock type="diamond_block"/>
#                     <FloorBlock type="air"/>
#                     <GapBlock type="air"/>
#                     <GapProbability>'''+str(gp)+'''</GapProbability>
#                     <AllowDiagonalMovement>false</AllowDiagonalMovement>
#                   </MazeDecorator>
#                   <ServerQuitFromTimeUp timeLimitMs="10000"/>
#                   <ServerQuitWhenAnyAgentFinishes/>
#                 </ServerHandlers>
#               </ServerSection>
# 
#               <AgentSection mode="Survival">
#                 <Name>Wallace</Name>
#                 <AgentStart>
#                     <Placement x="0.5" y="56.0" z="0.5" yaw="0"/>
#                 </AgentStart>
#                 <AgentHandlers>
#                     <DiscreteMovementCommands/>
#                     <AgentQuitFromTouchingBlockType>
#                         <Block type="redstone_block"/>
#                     </AgentQuitFromTouchingBlockType>
#                     <ObservationFromGrid>
#                       <Grid name="floorAll">
#                         <min x="-10" y="-1" z="-10"/>
#                         <max x="10" y="-1" z="10"/>
#                       </Grid>
#                   </ObservationFromGrid>
#                 </AgentHandlers>
#               </AgentSection>
#             </Mission>'''

def maze(seed = "0"):
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
        <Summary>This is the Wallace AI, it runs faster then HongKong Journalism</Summary>
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
            </DrawingDecorator>
            <ServerQuitWhenAnyAgentFinishes/>
        </ServerHandlers>
    </ServerSection>
              
    <AgentSection mode="Survival">
        <Name>Wallace</Name>
        <AgentStart>
            <Placement x="11" y="13" z="11" yaw="0"/>
            <Inventory>
                <InventoryItem slot="8" type="diamond_pickaxe"/>
            </Inventory>
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    