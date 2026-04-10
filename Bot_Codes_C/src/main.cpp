/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       harri                                                     */
/*    Created:      4/9/2026, 9:34:59 PM                                      */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/
#include "vex.h"

using namespace vex;

// A global instance of vex::brain used for printing to the V5 brain screen
vex::brain       Brain;
vex::controller   Controller( controllerType::primary);


// define your global instances of motors and other devices here
vex::motor      Motor1( vex::PORT1, vex::gearSetting::ratio18_1, false );
vex::motor      Motor2( vex::PORT2, vex::gearSetting::ratio18_1, false );
vex::motor      Motor3( vex::PORT3, vex::gearSetting::ratio18_1, false );
vex::motor      Motor4( vex::PORT4, vex::gearSetting::ratio18_1, false );
vex::motor      Motor5( vex::PORT5, vex::gearSetting::ratio18_1, false );
vex::motor      Motor6( vex::PORT6, vex::gearSetting::ratio18_1, false );

vex::motor     elevator( vex::PORT7, vex::gearSetting::ratio36_1, false );

vex::motor     tintake( vex::PORT8, vex::gearSetting::ratio18_1, false );
vex::motor     tintake2( vex::PORT9, vex::gearSetting::ratio18_1, true );

vex::motor     bintake( vex::PORT10, vex::gearSetting::ratio6_1, false );
vex::motor     bintake2( vex::PORT11, vex::gearSetting::ratio6_1, true );

vex::motor_group Tintake( tintake, tintake2 );
vex::motor_group Bintake( bintake, bintake2 );

vex::motor_group   LeftDrive( Motor1, Motor2, Motor3 );
vex::motor_group   RightDrive( Motor4, Motor5, Motor6 );

void Motor_In(int speed, vex::motor_group &motorGroup ){
    if (speed > 0) {
        motorGroup.spin( directionType::fwd, speed, percentUnits::pct );
    } else if (speed < 0) {
        motorGroup.spin( directionType::rev, -speed, percentUnits::pct );
    } else {
        motorGroup.stop();
    }
}

void belt_mismatch(vex::motor belt1, vex::motor belt2) {
    if (belt1.position(rotationUnits::deg) != belt2.position(rotationUnits::deg)) {

        Brain.Screen.setCursor( 3, 1);
        Brain.Screen.print("Belt Mismatch Fixing: %f, %f", belt1.position(rotationUnits::deg), belt2.position(rotationUnits::deg) );
        belt1.spinTo( belt2.position(rotationUnits::deg), rotationUnits::deg, 100, velocityUnits::pct );

    }
   
}


int main() {

    while(true) {
        Brain.Screen.setCursor(1,1);
        Brain.Screen.print("Hello V5 in C++" );

        int Foward_Back = Controller.Axis3.position( percentUnits::pct );
        int Strafe = Controller.Axis1.position( percentUnits::pct );

        int LeftSpeed = Foward_Back + Strafe;
        int RightSpeed = Foward_Back - Strafe;

        Motor_In(LeftSpeed, LeftDrive);
        Motor_In(RightSpeed, RightDrive);

        bool R1pressed = Controller.ButtonR1.pressing();
        bool R2pressed = Controller.ButtonR2.pressing();
        bool L1pressed = Controller.ButtonL1.pressing();
        bool L2pressed = Controller.ButtonL2.pressing();

        bool Xpressed = Controller.ButtonX.pressing();
        bool Bpressed = Controller.ButtonB.pressing();

        if (R1pressed) {
            Tintake.spin( directionType::fwd, 100, percentUnits::pct );
           
            
            
        } else if (L1pressed) {
            Tintake.spin( directionType::rev, 100, percentUnits::pct );
        }
        else if (Xpressed) {
            Tintake.spin( directionType::fwd, 100, percentUnits::pct );
            Bintake.spin( directionType::fwd, 100, percentUnits::pct );
        } else if (Bpressed) {
            Tintake.spin( directionType::rev, 100, percentUnits::pct );
            Bintake.spin( directionType::rev, 100, percentUnits::pct );
        } else {
            Tintake.stop(brakeType::hold);
            
        }


        if (R2pressed) {
            Bintake.spin( directionType::fwd, 100, percentUnits::pct );
            
        } else if (L2pressed) {
            Bintake.spin( directionType::rev, 100, percentUnits::pct );

           
        } 
        else if (Xpressed) {
            Tintake.spin( directionType::fwd, 100, percentUnits::pct );
            Bintake.spin( directionType::fwd, 100, percentUnits::pct );
        } else if (Bpressed) {
            Tintake.spin( directionType::rev, 100, percentUnits::pct );
            Bintake.spin( directionType::rev, 100, percentUnits::pct );
        } else {
            Bintake.stop(brakeType::hold);
            
        }

        if (R1pressed || R2pressed || Xpressed){
            elevator.spin( directionType::fwd, 100, percentUnits::pct );
        } else if (L1pressed || L2pressed || Bpressed) {
            elevator.spin( directionType::rev, 100, percentUnits::pct );
        } else {
            elevator.stop(brakeType::hold);
        }
        
        if (not R1pressed && not L1pressed && not R2pressed && not L2pressed && not Xpressed && not Bpressed) {
            belt_mismatch( tintake, tintake2 );
            belt_mismatch( bintake, bintake2 );
        }
        
        wait(20, msec); // Sleep the task for a short amount of time to prevent wasted resources.
    }
}
