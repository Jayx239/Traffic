from abc import abstractmethod


class Sandbox:
    def __init__(self):
        self.map = Map()
        self.configuration = Configuration


sandbox = Sandbox()
def getSandboxInstance(self):
    if self.sandbox:
        return self.sandbox
    self.sandbox = Sandbox()
    return self.sandbox

# configuration
class ConfigurationSingleton:
    def __init__(self,timestep):
        self.timestep = timestep
        self.configuration = self

Configuration = ConfigurationSingleton(1)

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
class Tickable:
    def __init__(self):
        return
    @abstractmethod
    def tick(self):
        pass

class Physics:
    def __init__(self,position,velocity,acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

class car(Tickable):
    def __init__(self):
        self.spedomiter = Spedomiter()
        self.engine = Engine()

    def tick(self):
        distance = self.engine.tick()
        measurement = Measurement(distance,self.engine.velocity,self.engine.acceleration)
        self.spedomiter.addMeasurement(measurement)
        return True

# Spedomiter
#   Used for tracking cars motion statistics
class Measurement:
    def __init__(self, distance,velocity,acceleration):
        self.distance = distance
        self.velocity = velocity
        self.acceleration = acceleration

class Engine:
    def __init__(self):
        self.velocity = 0
        self.acceleration = 0
        self.max_acceleration = 0
        self.max_velocity = 0
        self.acceleration = 0
        self.max_acceleration = 0;
        self.last_distance = 0;
    def tick(self):
        timeStep = Configuration.timestep
        max_delta_v = self.acceleration * timeStep
        if (max_delta_v+self.velocity) > self.max_velocity:
            self.acceleration = (self.max_velocity - self.velocity)/timeStep
        distance = (self.velocity + (.5*self.acceleration*timeStep)) * timeStep
        self.velocity += (self.acceleration)*(timeStep)
        self.last_distance = distance
        return distance

class Spedomiter:
    def __init__(self):
        self.time = 0
        self.distance = 0
        self.measurements = [Measurement(0,0,0)]

    def currentMeasurement(self):
        return self.measurements[len(self.measurements)-1]


    def addMeasurement(self,measurement):
        self.measurements.append(measurement)
        self.time+=1
        self.distance+= measurement.distance
    def getSpeed(self):
        return self.measurements[len(self.measurements)-1]
    def describe(self):
        return "RunTime: " + str(self.time) + "\nDistance: " + str(self.distance) + "\nMeasurements:\n" + " Distance: " + str(self.currentMeasurement().distance) + "\n Speed: " + str(self.currentMeasurement().velocity) + "\n Acceleration: " + str(self.currentMeasurement().acceleration) + "\n"

# Track
class TrackNode:
    def __init__(self,top_node,left_node,bottom_node,right_node):
        self.nodes = [top_node,left_node,bottom_node,right_node]


class RoadSegment:
    def __init__(self,node,max_velocity):
        self.node = node
        self.MaxVelocity = max_velocity

class Road:
    def __init__(self):
        self.trackStart = TrackNode(None,None,None,None)
        self.trackPosition = self.trackStart
        self.trackPointer = Vector(Direction.right,1)

    def insertRoadSegment(self,segment):
        opositeDirection = ((self.trackPointer.direction+2)%4)
        segment.node.nodes[opositeDirection] = self.trackPosition.node.nodes[self.trackPointer.direction]
        self.trackPosition.node.nodes[self.trackPointer.direction] = segment
        self.trackPosition.node = segment

# Builder
class Population:
    def __init__(self):
        self.cars = []

class Map:
    def __init__(self):
        self.roads = []
        self.population = Population()

class Vector:
    def __init__(self,direction,magnitude):
        self.direction = direction
        self.magnitude = magnitude
