def world(seed = "0"):
    '''
    Document:   http://microsoft.github.io/malmo/0.21.0/Schemas/Mission.html#ns_xs
                http://microsoft.github.io/malmo/0.21.0/Documentation/index.html
    
    
    decorating methods:
        <DrawCuboid x1, y1, z1, x2, y2, z2, type/>
        <DrawLine x1, y1, z1, x2, y2, z2, type/>
        <DrawBlock x, y, z, type/>
        <DrawSphere x, y, z, radius, type/>
        <DrawItem x, y, z, type/>
        
        current world range:     x1 = "1" y1= "11" z1= "1" 
                                 x2= "20" y2= "15" z2= "20"
                                 
    
    1:bot left
    2:bot mid
    3.bot right
    
    4,5,6 mid
    
    7,8,9 top
    
    
    
    '''
    return'''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
    <About>
        <Summary>This is the Wallace AI, it runs faster than HongKong Journalism</Summary>
    </About>
              

    <ModSettings>
            <MsPerTick>100</MsPerTick>
        </ModSettings>
              
              
    <ServerSection>
        <ServerInitialConditions>
            <Weather>clear</Weather>
            <Time>
                <StartTime>6000</StartTime>
                <AllowPassageOfTime>false</AllowPassageOfTime>
            </Time>
        </ServerInitialConditions>
        <ServerHandlers>
            <FlatWorldGenerator generatorString="3;49,17,3,3,2;1;,biome_1"/>
            <DrawingDecorator>
                <DrawCuboid x1 = "0" y1= "9" z1= "0" x2= "30" y2= "15" z2= "30" type="brick_block"/>
                
                

                <DrawCuboid x1 = "1" y1= "11" z1= "1" x2= "9" y2= "20" z2= "9" type="air"/>
                <DrawCuboid x1 = "1" y1= "11" z1= "11" x2= "9" y2= "20" z2= "19" type="air"/>
                <DrawCuboid x1 = "1" y1= "11" z1= "21" x2= "9" y2= "20" z2= "29" type="air"/>
                
                <DrawCuboid x1 = "11" y1= "11" z1= "1" x2= "19" y2= "20" z2= "9" type="air"/>
                <DrawCuboid x1 = "11" y1= "11" z1= "11" x2= "19" y2= "20" z2= "19" type="air"/>
                <DrawCuboid x1 = "11" y1= "11" z1= "21" x2= "19" y2= "20" z2= "29" type="air"/>
                
                <DrawCuboid x1 = "21" y1= "11" z1= "1" x2= "29" y2= "20" z2= "9" type="air"/>
                <DrawCuboid x1 = "21" y1= "0" z1= "11" x2= "29" y2= "20" z2= "19" type="air"/>
                <DrawCuboid x1 = "21" y1= "11" z1= "21" x2= "29" y2= "20" z2= "29" type="air"/> 



                <DrawCuboid x1 = "25" y1= "11" z1= "5" x2= "25" y2= "11" z2= "5" type="bookshelf"/>
                <DrawCuboid x1 = "5" y1= "11" z1= "25" x2= "5" y2= "11" z2= "25" type="bookshelf"/>

                <DrawCuboid x1 = "20" y1= "11" z1= "5" x2= "20" y2= "13" z2= "5" type="diamond_block"/>

                <DrawCuboid x1 = "10" y1= "11" z1= "5" x2= "10" y2= "13" z2= "5" type="planks"/>

                <DrawCuboid x1 = "10" y1= "11" z1= "25" x2= "10" y2= "13" z2= "25" type="diamond_block"/>
                <DrawCuboid x1 = "20" y1= "11" z1= "25" x2= "20" y2= "13" z2= "25" type="planks"/>
                <DrawCuboid x1 = "11" y1= "10" z1= "1" x2= "19" y2= "10" z2= "9" type="brown_mushroom_block"/>
                <DrawCuboid x1 = "15" y1= "11" z1= "20" x2= "15" y2= "13" z2= "20" type="stone"/> 
                <DrawCuboid x1 = "15" y1= "11" z1= "10" x2= "15" y2= "13" z2= "10" type="sand"/> 
                <DrawCuboid x1 = "20" y1= "11" z1= "15" x2= "20" y2= "13" z2= "15" type="iron_block"/>
                <DrawCuboid x1 = "1" y1= "10" z1= "11" x2= "9" y2= "10" z2= "19" type="lava"/>
                <DrawCuboid x1 = "4" y1= "10" z1= "11" x2= "6" y2= "11" z2= "16" type="stone"/>
                <DrawCuboid x1 = "24" y1= "10" z1= "11" x2= "26" y2= "11" z2= "16" type="stone"/>
                
                <DrawItem x='26' y='11' z='26' type="gold_block"/>
                <DrawItem x='16' y='11' z='26' type="cake"/>
                
                <DrawItem x='2' y='11' z='2' type="dirt"/>
                
                <DrawItem x='11' y='11' z='15' type="ladder"/>
                <DrawItem x='16' y='11' z='16' type="tnt"/>
                <DrawItem x='13' y='11' z='13' type="redstone"/>
                
                
                
                <DrawCuboid x1 = "15" y1= "28" z1= "15" x2= "15" y2= "29" z2= "15" type="obsidian"/> 
            </DrawingDecorator>
            <ServerQuitWhenAnyAgentFinishes/>
        </ServerHandlers>
    </ServerSection>
              
    <AgentSection mode="Survival">
        <Name>Wallace</Name>
        <AgentStart>
            <Placement x="15" y="12" z="15" yaw="-90"/>
            <Inventory>
                <InventoryItem slot="9" type="planks" variant="acacia"/>
                <InventoryItem slot="10" type="brown_mushroom"/>
                <InventoryItem slot="11" type="planks" variant="spruce"/>
                <InventoryItem slot="12" type="brown_mushroom"/>
            </Inventory>
        </AgentStart>
        <AgentHandlers>
            <VideoProducer
            want_depth="0"
            viewpoint="1">
                <Width> 1200 </Width>
                <Height> 720 </Height>
                <DepthScaling
                min="0"
                max="1"
                autoscale="0"/>
            </VideoProducer>
            <AbsoluteMovementCommands/>
            <SimpleCraftCommands/>
            <MissionQuitCommands/>
            <InventoryCommands/>
            <ObservationFromNearbyEntities>
                <Range name="entities" xrange="40" yrange="40" zrange="40"/>
            </ObservationFromNearbyEntities>
            <ObservationFromFullInventory/>
            <AgentQuitFromCollectingItem>
                <Item type="rabbit_stew" description="Supper's Up!!"/>
            </AgentQuitFromCollectingItem>
        </AgentHandlers>
    </AgentSection>
    </Mission>'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    