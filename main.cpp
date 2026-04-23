/*----------------------------------------------------------------------------------*/
/*                                                                                  */
/*    Module:             main.cpp                                                  */
/*    Author:             VEX                                                       */
/*    Created:            Wed Jun 09 2021                                           */
/*    Description:        Drive to Location (Using Tangents)                        */
/*                        This example will show how to use a GPS Sensor to         */
/*                        navigate a V5 Moby Hero Bot to the center of the field    */
/*                        by using a tangent calculation to determine the heading   */
/*                        to drive towards                                          */
/*                                                                                  */
/*    Starting Position:  Any                                                       */
/*                                                                                  */
/*----------------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Drivetrain           drivetrain    1, 10, 3        
// ForkMotorGroup       motor_group   2, 9            
// Rotation4            rotation      4               
// GPS8                 gps           8               
// DistanceLeft         distance      12              
// DistanceRight        distance      20              
// Optical19            optical       19              
// BumperA              bumper        A               
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
motor LeftDriveSmart = motor(PORT1, ratio18_1, false);
motor RightDriveSmart = motor(PORT10, ratio18_1, true);
inertial DrivetrainInertial = inertial(PORT3);
smartdrive Drivetrain = smartdrive(LeftDriveSmart, RightDriveSmart, DrivetrainInertial, 319.19, 320, 40, mm, 1);
motor ForkMotorGroupMotorA = motor(PORT2, ratio18_1, false);
motor ForkMotorGroupMotorB = motor(PORT9, ratio18_1, true);
motor_group ForkMotorGroup = motor_group(ForkMotorGroupMotorA, ForkMotorGroupMotorB);
rotation Rotation4 = rotation(PORT4, false);
gps GPS8 = gps(PORT8, 0.00, -240.00, mm, 180);
distance DistanceLeft = distance(PORT12);
distance DistanceRight = distance(PORT20);
optical Optical19 = optical(PORT19);
bumper BumperA = bumper(Brain.ThreeWirePort.A);

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
  DrivetrainInertial.calibrate();
  Brain.Screen.print("Calibrating Inertial for Drivetrain");
  // wait for the Inertial calibration process to finish
  while (DrivetrainInertial.isCalibrating()) {
    wait(25, msec);
  }
  // reset the screen now that the calibration is complete
  Brain.Screen.clearScreen();
  Brain.Screen.setCursor(1,1);
  wait(50, msec);
  Brain.Screen.clearScreen();
}

void printPosition() {
  // Print GPS position values to the V5 Brain
  Brain.Screen.print("X: %.2f", GPS8.xPosition(mm));
  Brain.Screen.print("  Y: %.2f", GPS8.yPosition(mm));
  Brain.Screen.newLine();
}

int main() {
  // Calibrate the GPS before starting
  GPS8.calibrate();
  while (GPS8.isCalibrating()) { task::sleep(50); }

  // Orient the drivetrain's heading with the GPS heading
  Drivetrain.setHeading(GPS8.heading(), degrees);
  Drivetrain.setTurnVelocity(25, percent);

  // Print the starting position of the robot
  printPosition();

  // Store the current position of the robot
  float startingX = GPS8.xPosition(mm);
  float startingY = GPS8.yPosition(mm);

  // Store the target ending position of the robot
  float endingX = -304;
  float endingY = 608.3;

  // Implement atan2 to calculate the heading that the robot needs to
  // turn to in order to drive towards the ending position
  float turnAngle = atan((endingX - startingX) / (endingY - startingY)) * 180 / M_PI;
  if (endingY - startingY < 0) {
    turnAngle = turnAngle + 180;
  }

  // Turn the robot to face the ending position
  Drivetrain.turnToHeading(turnAngle, degrees, true);

  // Calculate the drive distance needed, then drive towards the target position
  float driveDistance = sqrt(((endingX - startingX) * (endingX - startingX)) + ((endingY - startingY) * (endingY - startingY)));

  Drivetrain.driveFor(forward, driveDistance, mm, true);
  
  // Print the ending position of the robot
  printPosition();
}