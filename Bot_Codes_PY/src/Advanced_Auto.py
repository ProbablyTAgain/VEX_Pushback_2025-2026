from vex import *

brain = Brain()
controller = Controller()
Radio = VexlinkType.GENERIC

distanceS = Distance(Ports.PORT21)

motor1 = Motor(Ports.PORT1, GearSetting.RATIO_36_1, False)
motor2 = Motor(Ports.PORT2, GearSetting.RATIO_36_1, False)
motor3 = Motor(Ports.PORT3, GearSetting.RATIO_36_1, False)
motor4 = Motor(Ports.PORT4, GearSetting.RATIO_36_1, False)
motor5 = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
motor6 = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)


left = MotorGroup(motor1, motor2, motor3)
right = MotorGroup(motor4, motor5, motor6)

AWD = DriveTrain(left, right, 12.9, 16.5, 12.5, INCHES, 1.4) 


def auto():

    AWD.drive(FORWARD)
    wait(2, SECONDS)
    AWD.stop(BrakeType.BRAKE)
    AWD.turn_for(LEFT, 90, DEGREES)

    while True:

        Walldistance = distanceS.object_distance(INCHES)

        brain.screen.set_cursor(1,1)
        brain.screen.print("Dist from wall: ",Walldistance, " IN")

        if Walldistance <= 5:

            brain.screen.set_cursor(2,1)
            brain.screen.print("5 IN or less from wall, stopping")
            AWD.stop(BrakeType.BRAKE)
            
        
        
        AWD.turn_for(LEFT, 90, DEGREES)
        AWD.drive_for(FORWARD, 2, INCHES)

        if Walldistance <= .5:

            brain.screen.set_cursor(3,1)
            brain.screen.print("0.5 IN or less from loader")
            AWD.stop(BrakeType.BRAKE)

        DistanceTraveled = motor1.position(DEGREES) + motor2.position(DEGREES) + motor3.position(DEGREES) + motor4.position(DEGREES) + motor5.position(DEGREES) + motor6.position(DEGREES)
        brain.screen.set_cursor(4,1)
        brain.screen.print("Distance traveled in DEGREES: ", DistanceTraveled)
        break

auto()