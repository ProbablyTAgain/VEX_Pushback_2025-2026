from vex import *

brain = Brain()
controller = Controller()
Radio = VexlinkType.GENERIC

# Wheel motors
motor1L = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)
motor2L = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
motor3L = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True)

motor4R = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
motor5R = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
motor6R = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)

netbelt = Motor(Ports.PORT18, GearSetting.RATIO_36_1, True)

intakefan = Motor(Ports.PORT12, GearSetting.RATIO_36_1, True)
intakefan2 = Motor(Ports.PORT17, GearSetting.RATIO_36_1, False)

intakefans = MotorGroup(intakefan, intakefan2)
Topbelt = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)

#Grouping motors for drive
left_side = MotorGroup(motor1L, motor2L, motor3L)
right_side = MotorGroup(motor4R, motor5R, motor6R)

drivetrain = DriveTrain(left_side, right_side, 329, 419.1, 317.5, MM)



def Motor_Input(side, speed):
        if speed > 0:
            side.spin(FORWARD, min(abs(speed), 40), VelocityUnits.PERCENT)
        elif speed < 0:
            side.spin(REVERSE, min(abs(speed), 40), VelocityUnits.PERCENT)
        else:
            side.stop(BrakeType.COAST)


def auto():
    # drivetrain.set_stopping(HOLD)
    # wait(2,SECONDS)
    # drivetrain.drive_for(FORWARD, 12, INCHES, 20, PERCENT)
    # wait(2,SECONDS)
    # drivetrain.turn_for(LEFT, 90, DEGREES, 25, PERCENT, True)
    
    # wait(2,SECONDS)
    # drivetrain.turn_for(LEFT, 90, DEGREES, 25, PERCENT, True)
    
    # wait(2,SECONDS)
    # drivetrain.turn_for(LEFT, 90, DEGREES, 25, PERCENT, True)
    # wait(2,SECONDS)
    # drivetrain.turn_for(LEFT, 90, DEGREES, 25, PERCENT, True)
    intakefans.spin(FORWARD)
    wait(2, SECONDS)
    intakefans.stop(BrakeType.COAST)


def arcade_drive():
    while True:
            Forwardback = controller.axis3.position()
            turn = controller.axis1.position()

            left_speed = Forwardback + turn
            right_speed = Forwardback - turn

            R1Pressed = controller.buttonR1.pressing()
            L1Pressed = controller.buttonL1.pressing()
            R2Pressed = controller.buttonR2.pressing()
            L2Pressed = controller.buttonL2.pressing()

            if R2Pressed:
                netbelt.spin(FORWARD, 100, VelocityUnits.PERCENT)
                intakefans.spin(FORWARD, 100, VelocityUnits.PERCENT)
            elif L2Pressed:
                netbelt.spin(REVERSE, 100, VelocityUnits.PERCENT)
                intakefans.spin(REVERSE, 100, VelocityUnits.PERCENT)
            else:
                netbelt.stop(BrakeType.COAST)
                intakefans.stop(BrakeType.COAST)

            if R1Pressed:
                Topbelt.spin(REVERSE, 100, VelocityUnits.PERCENT)
            elif L1Pressed:
                Topbelt.spin(FORWARD, 100, VelocityUnits.PERCENT)
            else:
                Topbelt.stop(BrakeType.COAST)

            Motor_Input(left_side, left_speed)
            Motor_Input(right_side, right_speed)


if __name__ == "__main__":

    Competition(arcade_drive, auto)
