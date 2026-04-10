from vex import *

brain = Brain()
controller = Controller()
Raido = VexlinkType.MANAGER


def Drive():
    # Initialize all drivetrain motors
    motor1 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
    motor2 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
    motor3 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
    motor4 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)

    # Left and right motor groups
    left_side = MotorGroup(motor1, motor4)
    right_side = MotorGroup(motor2, motor3)

    return [left_side, right_side]


def Arcade_Drive( deadzone=5, timeout_ms= 5000):
     
     
    # Print to brain screen to show user control has started
     brain.screen.print("User Control")
     # Get motor groups
     motor_groups = Drive()
     left_side = motor_groups[0]
     right_side = motor_groups[1]

     idle = 0  # set idle to 0 at start of user control
     while True:
        # Read joystick positions 
        forward_back = controller.axis3.position()
        turn = controller.axis1.position()

        # Calculate motor speeds
        left_speed = forward_back + turn
        right_speed = forward_back - turn

            # Apply deadzone
        if abs(left_speed) <= deadzone:
                left_speed = 0
        if abs(right_speed) <= deadzone:
                right_speed = 0

        # If both joysticks are resting break loop
        if left_speed == 0 and right_speed == 0:
                idle += 20  # Add 20 until timeout at 5000 or 5 seconds
        else:
                idle = 0  # Reset if any joystick moves
                
        if idle >= timeout_ms:
                break

        # Set velocities (use absolute because direction given by spin)
        left_side.set_velocity(abs(left_speed), VelocityUnits.PERCENT)
        right_side.set_velocity(abs(right_speed), VelocityUnits.PERCENT)

        # Funtion to take input and convert it to motor power
        def Motor_Input(speed, side):
                if speed > 0:
                    side.spin(FORWARD)
                elif speed < 0:
                    side.spin(REVERSE)
                else:
                    side.stop(BrakeType.COAST)
            
        # Display joystick values on brain screen (line 2, collum 1)
       

        # Apply motor inputs
        Motor_Input(left_speed, left_side)

        Motor_Input(right_speed, right_side)

        wait(20, TimeUnits.MSEC)  # Small delay for smoother updates

if __name__ == "__main__":
   
    def main():
        Arcade_Drive()
    main()