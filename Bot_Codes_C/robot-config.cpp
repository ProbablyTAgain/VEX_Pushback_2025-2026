#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

motor Right_Top( PORT18, gearSetting::ratio6_1, false);
motor Right_Middle(PORT19, gearSetting::ratio6_1, true);
motor Right_Bottom(PORT20, gearSetting::ratio6_1, false);

motor Left_Top(PORT8, gearSetting::ratio6_1, false);
motor Left_Middle(PORT9, gearSetting::ratio6_1, false);
motor Left_Bottom(PORT10, gearSetting::ratio6_1, false);

motor_group LeftDrive(Left_Top,Left_Middle,Left_Bottom);
motor_group RightDrive(Right_Top, Right_Middle,Right_Bottom);

smartdrive Drivetrain(LeftDrive, RightDrive, GPS8,12.57,15, 22, inches,1.8);
// VEXcode generated functions



/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  Brain.Screen.print("Device initialization...");
  Brain.Screen.setCursor(2, 1);
  // calibrate the drivetrain Inertial
  wait(200, msec);
  GPS8.calibrate();
  Brain.Screen.print("Calibrating Inertial for Drivetrain");
  // wait for the Inertial calibration process to finish
  while (GPS8.isCalibrating()) {
    wait(25, msec);
  }
  // reset the screen now that the calibration is complete
  Brain.Screen.clearScreen();
  Brain.Screen.setCursor(1,1);
  wait(50, msec);
  Brain.Screen.clearScreen();
}