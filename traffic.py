
# Physics
class Direction:
    top = 0
    left = 1
    bottom = 2
    right = 3

class location:
    def __init__(self,x,y):
        self.position_x = x
        self.position_y = y
        
    position_x = 0
    position_y = 0


class velocity:
    def __init__(self,x,y):
        self.velociy_x = x
        self.velocity_y = y
    
    veloctiy_x = 0
    velocity_y = 0

class acceleration:
    def __intit__(self,x,y):
        self.acceleration_x = x
        self.acceleration_y = y

    acceleration_x = 0
    acceleration_y = 0

class physics:
    def __init__(self,position,velocity,acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

class car(physics):
    def __init__(self,position,velocity,acceleration):
        super(self,position,velocity,acceleration).__init__()

# Track
class TrackNode:
    def __init__(self,top_node,left_node,bottom_node,right_node):
        #self.top_node = top_node
        #self.left_node = left_node
        #self.bottom_node = bottom_node
        #self.right_node = right_node
        self.nodes = [top_node,left_node,bottom_node,right_node]
    #def getNode(self,direction):
        #if direction = Direction.top:
         #   return self.top_node
        #elif direction = direction.left:
         #   return self.left_node
        #elif direction = direction.bottom:
        #    return self.bottom_node
        #elif direction = 

class RoadSegment:
    def __init__(self,node,max_velocity)
        self.node = node
        self.MaxVelocity = max_velocity

class Road:
    def __init__(self):
        self.trackStart = new TrackNode(None,None,None,None)
        self.trackPosition = trackStart
        self.trackPointer = new Vector(Direction.right,1)

    def insertRoadSegment(self,segment):
        opositeDirection = ((trackPointer.direction+2)%4)
        segment.node.nodes[opositeDirection] = trackPosition.node.nodes[trackPointer.direction]
        trackPosition.node.nodes[trackPointer.direction] = segment
        trackPosition.node = segment
    


# Builder
class Population:
    def __init__(self):
        self.cars = []

class Map:
    def __init__(self):
        self.roads = []
        self.population = new Population()
        
class Sandbox:
    def __init__(self):
        self.map = new Map()
        self.configuration = getConfigurationInstance()
    

sandbox = None
def getSandboxInstance(self):
    if(sandbox)
        return sandbox
    sandbox = new Sandbox()
    return sandbox

class Vector:
    def __init__(self,direction,magnitude):
        self.direction = direction
        self.magnitude = magnitude


# configuration
class configurationsingleton:
    def __init__(self,timestep):
        self.timestep = timestep
        self.configuration = self

Configuration = None
def getConfigurationInstance()
    if Configuration == None:
        Configuration = new ConfigurationSingleton(1);
    return Configuration
