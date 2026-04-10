/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       harri                                                     */
/*    Created:      4/9/2026, 11:21:06 PM                                     */
/*    Description:  V5 project                                                */
/*                                                                            */
/*----------------------------------------------------------------------------*/
#include "vex.h"

using namespace vex;

// A global instance of vex::brain used for printing to the V5 brain screen
vex::brain       Brain;
vex::controller   Controller1 = vex::controller(primary);

// define your global instances of motors and other devices here
vex::distance DistanceS = vex::distance( vex::PORT1 );

int main() {

   
    while(true) {
        int Wall_Distance = DistanceS.objectDistance( distanceUnits::cm );

            Brain.Screen.clearScreen();
            Brain.Screen.setCursor(1,1);
            Brain.Screen.print("Distance: %d", Wall_Distance);
       wait(20, msec); // Sleep the task for a short amount of time to prevent wasted resources.
    }
}
