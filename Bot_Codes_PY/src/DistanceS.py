from vex import *

brain = Brain()
controller = Controller()
Radio = VexlinkType.GENERIC


distanceS = Distance(Ports.PORT1)

while True:
    Walldistance = distanceS.object_distance(INCHES)

    brain.screen.set_cursor(1,1)
    brain.screen.print("Dist: ",Walldistance)
    if Walldistance <= 1:
        brain.screen.set_cursor(2,1)
        brain.screen.print("Wall Crash")
    else:
        brain.screen.clear_line(2)