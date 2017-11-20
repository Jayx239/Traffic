import traffic

TrafficSandbox = traffic.sandbox
TrafficSandbox.map = traffic.Map()
TrafficSandbox.configuration = traffic.Configuration


output = ""
car = traffic.car()
car.engine.max_velocity= 65
car.engine.max_acceleration = 1
car.engine.acceleration = 2.9
print(car.spedomiter.describe())
for currentTime in range(0,50):
    car.tick()
    print(car.spedomiter.describe())
    for step in range(0,car.engine.last_distance):
        output += "-"
    output += "*"
print("Distance vs Time")
print(output)
print("Distance Per Interval")
outputSplit = output.split("*")
for line in outputSplit:
    if line:
        print(line + "*")
