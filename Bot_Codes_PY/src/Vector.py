from vex import *

brain = Brain()
controller = Controller()
Radio = VexlinkType.GENERIC




elevator = Motor(Ports.PORT16, GearSetting.RATIO_36_1, True)

# Wheel motors
motor1LT = Motor(Ports.PORT18, GearSetting.RATIO_6_1, True)
motor2LB = Motor(Ports.PORT17, GearSetting.RATIO_6_1, False)

motor3RT = Motor(Ports.PORT6, GearSetting.RATIO_6_1,True)
motor4RB = Motor(Ports.PORT7, GearSetting.RATIO_6_1, False)

#Intake Top motos
intakeT = Motor(Ports.PORT13, GearSetting.RATIO_18_1, True)
intakeT2 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)

#Intake Bottom motos
intakeB = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
intakeB2 = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)

# motor groups for intakes
IntakeT = MotorGroup(intakeT, intakeT2)
IntakeB = MotorGroup(intakeB, intakeB2)

#Grouping motors for drive
left_side = MotorGroup(motor1LT, motor2LB)
right_side = MotorGroup(motor3RT, motor4RB)




# def autonomous():
    
#     drivetrain = DriveTrain(right_side, left_side, 12.57, 14.5, 11.5, DistanceUnits.IN, 1)
#     drivetrain.set_stopping(BrakeType.HOLD)
#     drivetrain.drive_for(FORWARD, 12, INCHES, 200, RPM)
#     drivetrain.turn_for(LEFT, 90, DEGREES, 50, RPM)
#     drivetrain.drive_for(FORWARD, 18, INCHES, 200, RPM)
#     drivetrain.turn_for(LEFT, 90, DEGREES, 50, RPM)
#     drivetrain.drive_for(FORWARD, 11.5, INCHES, 50 , RPM)
#     IntakeT.spin(REVERSE, 100, VelocityUnits.PERCENT)
#     IntakeB.spin(REVERSE, 100, VelocityUnits.PERCENT)
#     elevator.spin(REVERSE, 100, VelocityUnits.PERCENT)
#     wait(6, SECONDS)
#     IntakeB.stop(BrakeType.HOLD)
#     IntakeT.stop(BrakeType.HOLD)
#     elevator.stop(BrakeType.HOLD)
    
def arcade_drive():


    while True:
        
       
        Forwardback = controller.axis3.position()
        turn = controller.axis1.position()

        left_speed = Forwardback - turn
        right_speed = Forwardback + turn

    
        def Motor_Input(speed, side):
            if speed > 0:
                side.set_velocity(speed, VelocityUnits.PERCENT)
                side.spin(FORWARD, speed, VelocityUnits.PERCENT)
            elif speed < 0:
                side.set_velocity(speed, VelocityUnits.PERCENT)
                side.spin(REVERSE, abs(speed), VelocityUnits.PERCENT)
            else:
                side.stop(BrakeType.COAST)

        Motor_Input(left_speed, left_side)
        Motor_Input(right_speed, right_side)

        R1pressed = controller.buttonR1.pressing()
        L1pressed = controller.buttonL1.pressing()
        R2pressed = controller.buttonR2.pressing()
        L2pressed = controller.buttonL2.pressing()
        
        Xpressed = controller.buttonX.pressing()
        Bpressed = controller.buttonB.pressing()

       
        # Bottom intake control (R2/L2 priority, then X/B)
        if R2pressed:
            IntakeB.spin(FORWARD, 100, VelocityUnits.PERCENT)
        elif L2pressed:
            IntakeB.spin(REVERSE, 100, VelocityUnits.PERCENT)
        elif Xpressed:
            IntakeB.spin(FORWARD, 100, VelocityUnits.PERCENT)
            IntakeT.spin(FORWARD, 100 ,VelocityUnits.PERCENT)
        elif Bpressed:
            IntakeB.spin(REVERSE, 100, VelocityUnits.PERCENT)
            IntakeT.spin(REVERSE, 100, VelocityUnits.PERCENT)
        else:
            IntakeB.stop(BrakeType.HOLD)
            IntakeT.stop(BrakeType.HOLD)

        # Top intake control (R1/L1 priority, then X/B)
        if R1pressed:
            IntakeT.spin(FORWARD, 100, VelocityUnits.PERCENT)
        elif L1pressed:
            IntakeT.spin(REVERSE, 100, VelocityUnits.PERCENT)
        elif Xpressed:
            IntakeT.spin(FORWARD, 100, VelocityUnits.PERCENT)
            IntakeB.spin(FORWARD, 100, VelocityUnits.PERCENT)
        elif Bpressed:
            IntakeT.spin(REVERSE, 100, VelocityUnits.PERCENT)
            IntakeB.spin(REVERSE, 100, VelocityUnits.PERCENT)
        else:
            IntakeT.stop(BrakeType.HOLD)
            IntakeB.stop(BrakeType.HOLD)

        # Elevator control
        if R1pressed or R2pressed or Bpressed:
            elevator.spin(FORWARD, 100, VelocityUnits.PERCENT)
        elif L1pressed or L2pressed or Xpressed:
            elevator.spin(REVERSE, 100, VelocityUnits.PERCENT)
        else:
            elevator.stop(BrakeType.HOLD)
        
            

        wait(20, TimeUnits.MSEC)

arcade_drive()

