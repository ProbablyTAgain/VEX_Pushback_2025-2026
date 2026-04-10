from vex import *

brain = Brain()
controller = Controller()
Raido = VexlinkType.MANAGER



def Drive():
    # Initialize all drivetrain motors
    motor1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
    motor2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
    motor3 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
    motor4 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
    motor5 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True)
    motor6 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)

    
    return [motor1,motor2,motor3,motor4,motor5,motor6]



def Arcade_Drive():
    
    # Print to brain screen to show user control has started
    brain.screen.print("User Control")
    
    # Get motors
    motor = Drive()
  
    # Put motors into left and right side groups
    left_side = MotorGroup(motor[0], motor[1], motor[2])
    right_side = MotorGroup(motor[3],motor[4],motor[5])
    
    while True:
        # Read joystick positions 
        forward_back = controller.axis3.position()
        turn = controller.axis1.position()

        # Calculate motor speeds
        left_speed = forward_back - turn
        right_speed = forward_back + turn

               
       
        # Funtion to take input and convert it to motor power
        def Motor_Input(speed, side):
                        
            # Set velocities (use absolute)
            left_side.set_velocity(abs(left_speed), VelocityUnits.PERCENT)
            right_side.set_velocity(abs(right_speed), VelocityUnits.PERCENT)
            if speed > 0:
                side.spin(FORWARD, abs(speed), VoltageUnits.VOLT)
            elif speed < 0:
                side.spin(REVERSE, abs(speed), VoltageUnits.VOLT)
            else:
                side.stop(BrakeType.COAST)

        def Reduced_Speed(speed, side):
            if speed > 0:
                side.spin(FORWARD, 20, VelocityUnits.PERCENT)
            elif speed < 0:
                side.spin(REVERSE, 20, VelocityUnits.PERCENT)
            else:
                side.stop(BrakeType.COAST)

            
        L1_pressed = controller.buttonL1.pressing()
        if L1_pressed:

            #   Motors run at 20% when l1 is held down
            Reduced_Speed(left_speed, left_side)
            Reduced_Speed(right_speed, right_side)
            
            brain.screen.set_cursor(2,1)    
            brain.screen.print("Slow mode")
           
        else:
            # Clear slow mode message
            brain.screen.clear_line(2)

            # Apply motor inputs
            Motor_Input(left_speed, left_side)

            Motor_Input(right_speed, right_side)
            

        wait(20, TimeUnits.MSEC)  # Small delay for smoother updates

if __name__ == "__main__":
   
    def main():
        Arcade_Drive()
    main()