# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       harri                                                        #
# 	Created:      2/25/2026, 1:20:37 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports

from vex import *

brain = Brain()
controller = Controller()



def motors():

    elevator = Motor(Ports.PORT16, GearSetting.RATIO_36_1, True)

    # Wheel motors
    motor1LT = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
    motor2LB = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)

    motor3RT = Motor(Ports.PORT4, GearSetting.RATIO_6_1,True)
    motor4RB = Motor(Ports.PORT5, GearSetting.RATIO_6_1, False)

    #Intake Top motos
    intakeT = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
    intakeT2 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)

    #Intake Bottom motos
    intakeB = Motor(Ports.PORT8, GearSetting.RATIO_6_1, False)
    intakeB2 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, True)

    # motor groups for intakes
    IntakeT = MotorGroup(intakeT, intakeT2)
    IntakeB = MotorGroup(intakeB, intakeB2)

   #Grouping motors for drive
    left_side = MotorGroup(motor1LT, motor2LB)
    right_side = MotorGroup(motor3RT, motor4RB)
  
    intakeT.position(0, RotationUnits.DEG)
    intakeB.position(0, RotationUnits.DEG)
    motor_list = [elevator, left_side, right_side, IntakeT,IntakeB]
    return motor_list

def autonomous():
    motor = motors()
    intakeT = motor[3]
    intakeT.spin(FORWARD, 100, VelocityUnits.PERCENT)
    wait(2, TimeUnits.SECONDS)
    intakeT.stop(BrakeType.HOLD)
    return


    

def arcade_drive():
    motor = motors()
    left_side = motor[1]
    right_side = motor[2]
    elevator = motor[0]
    intakeT = motor[3]
    intakeB = motor[4]

    while True:
        
        Forwardback = controller.axis3.position()
        turn = controller.axis1.position()

        left_speed = Forwardback - turn
        right_speed = Forwardback + turn

    
        def Motor_Input(speed, side):
            
            
                if speed > 0:
                    side.set_velocity(abs(speed), VelocityUnits.PERCENT)
                    side.spin(FORWARD, abs(speed), VelocityUnits.PERCENT)
                elif speed < 0:
                    side.set_velocity(abs(speed), VelocityUnits.PERCENT)
                    side.spin(REVERSE, abs(speed), VelocityUnits.PERCENT)
                else:
                    side.stop(BrakeType.COAST)

        Motor_Input(left_speed, left_side)
        Motor_Input(right_speed, right_side)

        R1pressed = controller.buttonR1.pressing()
        L1pressed = controller.buttonL1.pressing()
        R2pressed = controller.buttonR2.pressing()
        L2pressed = controller.buttonL2.pressing()
    
            
        if R2pressed:
            intakeB.spin(FORWARD, 60, VelocityUnits.PERCENT)
       
        elif L2pressed:
            intakeB.spin(REVERSE, 60, VelocityUnits.PERCENT)
           
        else:
            intakeB.stop(BrakeType.HOLD)
            
        if R1pressed:
            intakeT.spin(FORWARD, 100, VelocityUnits.PERCENT)
           
        elif L1pressed:
            intakeT.spin(REVERSE, 100, VelocityUnits.PERCENT)
          
        else:
            intakeT.stop(BrakeType.HOLD)
          
        if R1pressed or R2pressed:
            elevator.spin(FORWARD, 100, VelocityUnits.PERCENT)
        elif L1pressed or L2pressed:
            elevator.spin(REVERSE, 100, VelocityUnits.PERCENT)
        else:
            elevator.stop(BrakeType.HOLD)
        
            

        wait(20, TimeUnits.MSEC)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    autonomous()
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, TimeUnits.MSEC )
    # Stop the autonomous control tasks
    

def vexcode_driver_function():
    # Start the driver control tasks
    arcade_drive()
    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, TimeUnits.MSEC )
    # Stop the driver control tasks


# register the competition functions
competition = Competition( vexcode_auton_function, vexcode_driver_function )