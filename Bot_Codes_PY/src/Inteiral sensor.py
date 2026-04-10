from vex import *

brain = Brain()
controller = Controller()
Radio = VexlinkType.GENERIC

inertialS = Inertial(Ports.PORT2)

motor1 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)

XAXIS = "orientationType.ROLL"
YAXIS = "orientationType.PITCH"
ZAXIS = "orientationType.YAW"

inertialS.calibrate()
    
while inertialS.is_calibrating():
        inertialS.set_heading(0, DEGREES)
        inertialS.set_rotation(0, DEGREES)
        
        
        wait(2, SECONDS)

motor1.spin_to_position(2, TURNS, True)
while True:

    

    rotation = inertialS.rotation()

    Xposition = inertialS.orientation(OrientationType.ROLL)
    Yposition = inertialS.orientation(OrientationType.PITCH)
    Zposition = inertialS.orientation(OrientationType.YAW)

    heading = inertialS.heading()
    
    brain.screen.set_cursor(1,1)
    brain.screen.print("Rotation: ", rotation)
    brain.screen.set_cursor(2,1)
    brain.screen.print("X: ", Xposition, " Y: ", Yposition, " Z: ", Zposition)
    brain.screen.set_cursor(3,1)
    brain.screen.print("Heading: ", heading)
    brain.screen.set_cursor(4,1)
    brain.screen.print("Motor Position: ", motor1.position(DEGREES))
   
    
    wait(100, MSEC)