from vex import *

brain = Brain()
contoller = Controller()
Radio = VexlinkType.MANAGER

# Initialize the pneumatics system in the function if using one but outside the loop
PM = Pneumatics(brain.three_wire_port.d)
while True:
    
    R1Pressed = contoller.buttonR1.pressing()
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