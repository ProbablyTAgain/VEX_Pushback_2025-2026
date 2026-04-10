from vex import *

brain = Brain()
controller = Controller()
Raido = VexlinkType.MANAGER

def Drive():
    # Initialize all drivetrain motors
    #
    motor1 = Motor(Ports.PORT1, GearSetting.RATIO_36_1, False)
    motor2 = Motor(Ports.PORT2, GearSetting.RATIO_36_1, True)
    motor3 = Motor(Ports.PORT11, GearSetting.RATIO_36_1, False)
    motor4 = Motor(Ports.PORT9, GearSetting.RATIO_36_1, False)
    motor5 = Motor(Ports.PORT10, GearSetting.RATIO_36_1, True)
    motor6 = Motor(Ports.PORT20, GearSetting.RATIO_36_1, True)

   

    T1 = motor1.temperature(TemperatureUnits.FAHRENHEIT)
    brain.screen.print(T1)
    
    return [motor1,motor2,motor3,motor4,motor5,motor6]



def Arcade_Drive( ):
     
    
   
    # Get motor groups
    motor_groups = Drive()
     
       # Left and right motor groups
    left_side = MotorGroup(motor_groups[0], motor_groups[1], motor_groups[2])
    right_side = MotorGroup(motor_groups[3],motor_groups[4],motor_groups[5])
    idle = 0  # set idle to 0 at start of user control
    
    while True:
        # Read joystick positions 
        forward_back = controller.axis3.position()
        turn = controller.axis1.position()

        # Calculate motor speeds
        left_speed = forward_back - turn
        right_speed = forward_back + turn

        # Read motor temperatures

        
        temp1 = motor_groups[0].temperature(TemperatureUnits.FAHRENHEIT)
      
        temp2 = motor_groups[1].temperature(TemperatureUnits.FAHRENHEIT)
        temp3 = motor_groups[2].temperature(TemperatureUnits.FAHRENHEIT)
        temp4 = motor_groups[3].temperature(TemperatureUnits.FAHRENHEIT)
        temp5 = motor_groups[4].temperature(TemperatureUnits.FAHRENHEIT)
        temp6 = motor_groups[5].temperature(TemperatureUnits.FAHRENHEIT)
    

        brain.screen.set_cursor(1,1)
        brain.screen.print("RR: ", str(temp1))
        brain.screen.set_cursor(2,1)
        brain.screen.print("RM: ", temp2)
        brain.screen.set_cursor(3,1)
        brain.screen.print("RF: ", temp3)
        brain.screen.set_cursor(4,1)
        brain.screen.print("LM: ", temp4)
        brain.screen.set_cursor(5,1)
        brain.screen.print("LR: ", temp5)
        brain.screen.set_cursor(6,1)
        brain.screen.print("LF: ", temp6)
        wait(.05, SECONDS)

        # Set velocities (use absolute because direction given by spin)
        left_side.set_velocity(abs(left_speed), VelocityUnits.PERCENT)
        right_side.set_velocity(abs(right_speed), VelocityUnits.PERCENT)

        # Funtion to take input and convert it to motor power
        def Motor_Input(speed, side):
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

            brain.screen.set_cursor(8,1)    
            brain.screen.print("Slow mode")
        

              
        L1_pressed = controller.buttonL1.pressing()
        if L1_pressed:
            #   Motors run at 20% when l1 is held down

            Reduced_Speed(left_speed, left_side)
            Reduced_Speed(right_speed, right_side)
        
        

        else:
            # Apply motor inputs
            Motor_Input(left_speed, left_side)

            Motor_Input(right_speed, right_side)

        wait(20, TimeUnits.MSEC)  # Small delay for smoother updates

if __name__ == "__main__":
   
    def main():
        Arcade_Drive()
    main()