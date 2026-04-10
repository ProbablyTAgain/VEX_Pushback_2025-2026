from vex import *

brain = Brain()
controller = Controller()

def Bot_Motors():
    motor1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
    motor2 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
    motor3 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
    motor4 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
    
    return [motor1, motor2, motor3, motor4]


def Regular_Drive(left_side, right_side):
    
    brain.screen.clear_screen()
    LeftJoy = controller.axis3.position()
    RightJoy = controller.axis2.position()

    left_side.set_velocity(abs(LeftJoy), VelocityUnits.PERCENT)
    right_side.set_velocity(abs(RightJoy), VelocityUnits.PERCENT)

    # Spin left group
    if LeftJoy > 0:
        left_side.spin(FORWARD)
    elif LeftJoy < 0:
        left_side.spin(REVERSE)
    else:
        left_side.stop(BrakeType.COAST)

    # Spin right group
    if RightJoy > 0:
        right_side.spin(REVERSE)
    elif RightJoy < 0:
        right_side.spin(FORWARD)
    else:
        right_side.stop(BrakeType.COAST)

    # Small delay to avoid input lag
    wait(20, TimeUnits.MSEC)



        


def Menchnum_Drive():
    Motor_list = Bot_Motors()
    motor1 = Motor_list[0]
    motor2 = Motor_list[1]
    motor3 = Motor_list[2]
    motor4 = Motor_list[3]  

    # Create motor groups 
    left_side = MotorGroup(motor1, motor3)
    right_side = MotorGroup(motor2, motor4)

   
    # Tool to stop motors
    def Stop_All_Motors():
        motor1.stop(BrakeType.COAST)
        motor2.stop(BrakeType.COAST)
        motor3.stop(BrakeType.COAST)
        motor4.stop(BrakeType.COAST)
    
    # Reset motor velocites after button is released
    def Reset_Motor_veloccity():
        motor1.set_velocity(0, VelocityUnits.PERCENT)
        motor2.set_velocity(0, VelocityUnits.PERCENT)
        motor3.set_velocity(0, VelocityUnits.PERCENT)
        motor4.set_velocity(0, VelocityUnits.PERCENT)
    
    # Set all velcitys to current left joystick value
    def set_all_motors_velocity(Velocity):
            motor1.set_velocity(abs(Velocity), VelocityUnits.PERCENT)
            motor2.set_velocity(abs(Velocity), VelocityUnits.PERCENT)
            motor3.set_velocity(abs(Velocity), VelocityUnits.PERCENT)
            motor4.set_velocity(abs(Velocity), VelocityUnits.PERCENT)

            
    while True:

        LeftJoy = controller.axis3.position()
        R1_Pressed = controller.buttonR1.pressing()
        L1_Pressed = controller.buttonL1.pressing()
        L2_Pressed = controller.buttonL2.pressing()
        R2_Pressed = controller.buttonR2.pressing()
        # If no toggles are pressed, run the regular drive 
        if not (R1_Pressed or L1_Pressed or L2_Pressed or R2_Pressed):
            Regular_Drive(left_side, right_side)
            # continue to next loop to keep checking toggles
            continue
       
        # Strafe Right
        if R1_Pressed: 
            set_all_motors_velocity(abs(LeftJoy))

            motor1.spin(FORWARD)
            motor3.spin(REVERSE)

           
            motor2.spin(REVERSE)
            motor4.spin(FORWARD)
            
            brain.screen.set_cursor(1,1)
            brain.screen.print("R1 Pressed - Strafing right")


            if not R1_Pressed:
                Reset_Motor_veloccity()
                Stop_All_Motors()
                
        elif not R1_Pressed:
            brain.screen.clear_line(1)
            

        # Strafe Left
        if L1_Pressed:
            set_all_motors_velocity(abs(LeftJoy))

            motor1.spin(REVERSE)
            motor3.spin(FORWARD)

            
            motor2.spin(FORWARD)
            motor4.spin(REVERSE)
        
            brain.screen.set_cursor(2,1)
            brain.screen.print("L1 Pressed: Strafing Left")

            if not L1_Pressed:
                Reset_Motor_veloccity()
                Stop_All_Motors()

        elif not L1_Pressed:
            brain.screen.clear_line(2)
       

        if L2_Pressed:

            motor1.set_velocity(abs(LeftJoy), VelocityUnits.PERCENT)
            motor2.set_velocity(abs(LeftJoy), VelocityUnits.PERCENT)

            motor1.spin(FORWARD)
            motor2.spin(REVERSE)

            brain.screen.set_cursor(3,1)
            brain.screen.print("L2 Pressed: Diagonal Left")

            if not L2_Pressed:
                Reset_Motor_veloccity()
                Stop_All_Motors()

        elif not L2_Pressed:
            brain.screen.clear_line(3)

        if R2_Pressed:
            motor4.set_velocity(abs(LeftJoy), VelocityUnits.PERCENT)
            motor3.set_velocity(abs(LeftJoy), VelocityUnits.PERCENT)


            motor4.spin(REVERSE)
            motor3.spin(FORWARD)
            
            brain.screen.set_cursor(4,1)
            brain.screen.print("R2 Pressed: Diagonal Right")

            if not R2_Pressed:
                Reset_Motor_veloccity()
                Stop_All_Motors()

        elif not R2_Pressed:
            brain.screen.clear_line(4)
       
        
       
       
        
          

if __name__ == "__main__":
    def main():
        Menchnum_Drive()

    main()
