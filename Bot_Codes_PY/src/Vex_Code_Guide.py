# Import vex library
# pressing control and clicking vex will show you all the functions and classes available to you in the vex library
from vex import *

# put brain in variable becomes easier to manipulate later, same goes for the controller and motors
brain = Brain()

controller = Controller()

#create motors, the first parameter is the port the motor is plugged into, the second parameter is the gear ratio, and the third parameter is 
#whether the motor is reversed(upside down) or not

motor1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
motor2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, True)
motor3 = Motor(Ports.PORT11, GearSetting.RATIO_6_1, False)
motor4 = Motor(Ports.PORT9, GearSetting.RATIO_6_1, False)
motor5 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, True)
motor6 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)

intakeT = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
intakeB = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)
elevator = Motor(Ports.PORT4, GearSetting.RATIO_36_1, True)

# Motor groups, this allows you to control multiple motors at the same time, in this case we are putting the left side motors in 
# one group and the right side motors in another group

left_side = MotorGroup(motor1, motor2, motor3)
right_side = MotorGroup(motor4, motor5, motor6)

All_Motors = MotorGroup(motor1, motor2, motor3, motor4, motor5, motor6)

# motor raitos and rpm speed

# RATIO_36_1 = 36:1 gear ratio, 100 rpm RED
# RATIO_18_1 = 18:1 gear ratio, 200 rpm GREEN
# RATIO_6_1 = 6:1 gear ratio, 600 rpm BLUE

# the main function that will run when the program is started
def main_or_other_name():

    # you can print to the brain screen to show the user what is going on, this is useful for debugging and for 
    # showing the user what mode they are in

    brain.screen.print("TEXT TO SHOW")

    brain.screen.set_cursor(2, 1) # set cursor to row 2, column 1 to print on the second line of the screen and so on
    brain.screen.print("MORE TEXT ON LINE 2")

    #You can also track the contorller joystick positions and print them to the brain screen, this is useful for 
    # debugging and for showing the user what the joystick positions are use a while true loop
    while True:
        # Read joystick positions 
        forward_back = controller.axis3.position()
        turn = controller.axis1.position()

        brain.screen.set_cursor(3, 1)
        brain.screen.print("Forward/Back: ", forward_back)

        brain.screen.set_cursor(4, 1)
        brain.screen.print("Turn: ", turn)

        # Basic arcade drive, this is a simple way to control the robot using the joystick,you can use the forward/backward joystick to 
        # control the forward and backward movement of the robot, and the left/right joystick to control the turning of the robot
        left_speed = forward_back - turn
        right_speed = forward_back + turn

        # Helper function to control the motors, this is a simple function that takes in a speed and a motor group and sets the velocity and 
        # spin direction of the motors based on the speed which is set by joystick input

        def Motor_Input(Joystick, side):
            
            
                if Joystick > 0:
                    side.set_velocity(abs(Joystick), VelocityUnits.PERCENT)
                    side.spin(FORWARD, abs(Joystick), VelocityUnits.PERCENT)
                elif Joystick < 0:
                    side.set_velocity(abs(Joystick), VelocityUnits.PERCENT)
                    side.spin(REVERSE, abs(Joystick), VelocityUnits.PERCENT)
                else:
                    side.stop(BrakeType.COAST)

        # load actual variables into the function
        Motor_Input(left_speed, left_side)
        Motor_Input(right_speed, right_side)

        # you can also control the motors using buttons, this is useful for controlling things like intakes and elevators, 
        # you can use the R1 and L1 buttons to control the top intake and the R2 and L2 buttons to control the bottom intake


        # Load these commands into variables to make it easier to read and manipulate later all pressing itdoes is check if the button is being held
        R1pressed = controller.buttonR1.pressing()
        L1pressed = controller.buttonL1.pressing()
        R2pressed = controller.buttonR2.pressing()
        L2pressed = controller.buttonL2.pressing()
    

        #if button pressed take action this can be print text or motor movements like so
        if R2pressed:
            intakeB.spin(FORWARD, 100, VelocityUnits.PERCENT)
       
        elif L2pressed:
            intakeB.spin(REVERSE, 100, VelocityUnits.PERCENT)
           
        else:
            # if neither button is being pressed stop the motor, you can change the brake type to COAST or HOLD depending on 
            # how you want the motor to stop
            intakeB.stop(BrakeType.HOLD)
            
        if R1pressed:
            intakeT.spin(FORWARD, 100, VelocityUnits.PERCENT)
           
        elif L1pressed:
            intakeT.spin(REVERSE, 100, VelocityUnits.PERCENT)
          
        else:
            intakeT.stop(BrakeType.HOLD)
        
        # you can also control multiple motors with the same buttons, for example you can use the R1 and R2 buttons to control 
        # the elevator as well as the intakes, this is useful for controlling multiple mechanisms at the same time
        if R1pressed or R2pressed:
            elevator.spin(FORWARD, 100, VelocityUnits.PERCENT)
        elif L1pressed or L2pressed:
            elevator.spin(REVERSE, 100, VelocityUnits.PERCENT)
        else:
            elevator.stop(BrakeType.HOLD)
        
            
        #delay so the brain doesnt get overloaded with commands and to make 
        # the program run smoother, you can adjust the delay time as needed
        wait(20, TimeUnits.MSEC)

# call to run program
main_or_other_name()


# Distence sensor example, this is how you can use the distance sensor to measure the distance to an object and 
# print it to the brain screen, you can also use the distance sensor to trigger actions based on the distance to an object, for example you can stop the robot if it gets too close to a wall
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
        break

# Pneumatics example, this is how you can use the pneumatics system to control a pneumatic piston and print the status to the brain screen, 
# you can also use the pneumatics system to trigger actions based on the status of the piston,
#  for example you can stop the robot if the piston is extended

# Initialize the pneumatics system in the function if using one but outside the loop
PM = Pneumatics(brain.three_wire_port.d)
while True:
    
    R1Pressed = controller.buttonR1.pressing()
    if R1Pressed:
        brain.screen.clear_line(2)
        PM.open()
        brain.screen.set_cursor(1,1)
        brain.screen.print("pppppppp")
        

    elif not R1Pressed:
        brain.screen.clear_line(1)
        PM.close()
        brain.screen.set_cursor(2,1)
        brain.screen.print("RRRRRRRRRRRR")

    
    wait(20, TimeUnits.MSEC)
    break

# Inertial sensor example, this is how you can use the inertial sensor to measure the rotation and orientation of the robot and 
# print it to the brain screen, you can also use the inertial sensor to trigger actions based on the rotation and orientation of the robot, 
# for example you can stop the robot if it tilts too much or if it rotates too much

inertialS = Inertial(Ports.PORT2)

XAXIS = "orientationType.ROLL"
YAXIS = "orientationType.PITCH"
ZAXIS = "orientationType.YAW"

inertialS.calibrate()
    
while inertialS.is_calibrating():
        inertialS.set_heading(0, DEGREES)
        inertialS.set_rotation(0, DEGREES)
        
        wait(2, SECONDS)

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
   
    wait(100, MSEC)
    break

#Limit switch example, this is how you can use the limit switch to detect when a 
# mechanism has reached a certain position and print the status to the brain screen
LMSW = Limit(brain.three_wire_port.d)
while True:
    if LMSW.pressing():
        brain.screen.next_row()
        brain.screen.print("Switch pressed")
        # You can also put an action here for the switch being pressed
    else:
        brain.screen.clear_line(3)
        break