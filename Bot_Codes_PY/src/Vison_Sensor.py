from vex import *
brain = Brain()
controller = Controller()
Radio = VexlinkType.MANAGER


def motors():
    belt = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
    trapdoor = DigitalOut(brain.three_wire_port.d)

    return [belt, trapdoor]


vexcode_visionsorter_objects = []
alianceMode = 0
 
def when_started1():

    VisionS__LIGHT_BLUE = Signature(1, -4283, -2847, -3565,5945, 10119, 8032,1.6, 0)
    VisionS__LIGHT_RED = Signature(2, 7895, 11809, 9852,-1351, 1, -675,1.6, 0)

    VisionS = Vision(Ports.PORT10, 60, VisionS__LIGHT_BLUE, VisionS__LIGHT_RED)

    global alianceMode, vexcode_visionsorter_objects
    alianceMode = 0
    
    motor_list = motors()

    belt_motor = motor_list[0]
    trapdoor = motor_list[1]
    
    
    
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Alliance: RED")

    while True:
        vexcode_visionsorter_objects = VisionS.take_snapshot(VisionS__LIGHT_RED)
        if vexcode_visionsorter_objects and len(vexcode_visionsorter_objects) > 0:
            trapdoor.set(False)
            belt_motor.set_max_torque(150, PERCENT)
            belt_motor.set_velocity(100, PERCENT)
            belt_motor.spin(FORWARD)
            brain.screen.set_cursor(2, 1)
            brain.screen.print("RED OBJECT DETECTED")
        else:
            brain.screen.clear_row(2)
            trapdoor.set(False)
            brain.screen.set_cursor(2, 1)
           
        vexcode_visionsorter_objects = VisionS.take_snapshot(VisionS__LIGHT_BLUE)

        if vexcode_visionsorter_objects and len(vexcode_visionsorter_objects) > 0:
            trapdoor.set(True)
            belt_motor.set_stopping(BRAKE)
            belt_motor.stop()
            brain.screen.set_cursor(2, 1)
            brain.screen.print("BLUE OBJECT DETECTED")
            
        else:
            brain.screen.clear_row(2)
            trapdoor.set(False)
            belt_motor.set_max_torque(150, PERCENT)
            belt_motor.set_velocity(100, PERCENT)
            belt_motor.spin(FORWARD)
            brain.screen.set_cursor(2, 1)
            brain.screen.print("NO BALL DETECTED")
        wait(5, MSEC)
 
when_started1()