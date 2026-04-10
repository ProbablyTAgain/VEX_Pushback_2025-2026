from vex import *

brain = Brain()
contoller = Controller()
Radio = VexlinkType.MANAGER

while True:
    PUM = brain.three_wire_port.b
    PM = DigitalOut(brain.three_wire_port.a)
    LMSW = Limit(brain.three_wire_port.d)

    if contoller.buttonR1.pressing():
        brain.screen.clear_line(2)
        PM.set(True)
        brain.screen.print("phumatic out")
        wait(2, SECONDS)
    else: 
        brain.screen.clear_line(1)
        PM.set(False)
        brain.screen.next_row()
        brain.screen.print("Phumatic in")
        wait(2, SECONDS)
    
    if LMSW.pressing():
        brain.screen.next_row()
        brain.screen.print("Switch")
    else:
        brain.screen.clear_line(3)