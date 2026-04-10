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
intakeB = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
intakeB2 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)

# motor groups for intakes
IntakeT = MotorGroup(intakeT, intakeT2)
IntakeB = MotorGroup(intakeB, intakeB2)

