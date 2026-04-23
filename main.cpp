/*----------------------------------------------------------------------------------*/
/*                                                                                  */
/*    Module:             main.cpp                                                  */
/*    Author:             VEX                                                       */
/*    Created:            Wed Jun 09 2021                                           */
/*    Description:        Drive to Location (Known Starting Position)               */
/*                        This example will show how to use a GPS Sensor to         */
/*                        navigate a V5 Moby Hero Bot to the center of a field      */
/*                        by driving along the X-axis then the Y-axis               */
/*                                                                                  */
/*    Starting Position:  Bottom Right Corner - Facing West                         */
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

void printPosition() {
  // Print GPS position values to the V5 Brain
  Brain.Screen.print("X: %.2f", GPS8.xPosition(mm));
  Brain.Screen.print("  Y: %.2f", GPS8.yPosition(mm));
  Brain.Screen.newLine();
}

int main() {
  // Calibrate the GPS Sensor before starting
  GPS8.calibrate();
  while (GPS8.isCalibrating()) { task::sleep(50); }

  // Set the approximate starting position of the robot
  // This helps the GPS Sensor know its starting position
  // if it is too close to the field walls to get an accurate initial reading

  // Orient the drivetrain's heading with the GPS heading
  Drivetrain.setHeading(GPS8.heading(), degrees);
  Drivetrain.setTurnVelocity(25, percent);
  
  //change to mm and face forward
  // GPS8.setLocation(-588.845, 1586.232, mm, 0, degrees);

  // Print the starting position of the robot
  printPosition();
  Drivetrain.drive(forward);

  /*
  // Keep driving until the GPS's reaches position 598.84
  while ((GPS8.yPosition(mm) < -598.84)) {
    wait(0.1, seconds);
  }
  Drivetrain.stop();

  Drivetrain.turnToHeading(90, degrees, true);
  Drivetrain.drive(forward);

  // Keep driving until the GPS's reaches position 907.427
  while ((GPS8.xPosition(mm) < -907.427)) {
    wait(0.1, seconds);
  }
  Drivetrain.stop();

  Drivetrain.turnToHeading(180, degrees, true);
  Drivetrain.drive(forward);

  // Keep driving until the GPS's reaches position 907.427
  while ((GPS8.yPosition(mm) > -684.784)) {
    wait(0.1, seconds);
  }
  Drivetrain.stop();

  // Print the ending position of the robot
  printPosition();

  // Store the current position of the robot
  float startingX = GPS8.xPosition(mm);
  float startingY = GPS8.yPosition(mm);

  // Store the target ending position of the robot
  float endingX = -274.002;
  float endingY = 274.002;

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
  */
}