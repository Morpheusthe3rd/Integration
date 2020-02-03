import time
import navigation_drivers_MM_interpreter_mk1
import motordrivers_mk2
import marvelmind
import sys
import Fundamentals

#This file plans to take the input from the Marvelmind beacons and the interpreter, and act on the movement recommendations from that
#interpreter. 

hedge = MarvelmindHedge(tty = "/dev/ttyACM0",adr=9, debug=False)
hedge.start()

My_hedge = hedge_positions()

#Assume that the robot is properly oriented

def main():
        
        #Motor 1 pins (assumed front right)
        Motor1 = Motor(17, 27)
        Motor1.front = True
        Motor1.right = True
        
        #Motor 2 pins (assumed back right)
        Motor2 = Motor(22,23)
        Motor2.right = True
        Motor2.back = True
        
        #Motor 3 pins (assumed front left)
        Motor3 = Motor(24,25)
        Motor3.left = True
        Motor3.front = True
        
        #Motor 4 pins (assumed back left)
        Motor4 = Motor(5,6)
        Motor4.left = True
        Motor4.back = True
        
        try:
                while True:
                        try:
                                My_hedge.update_position()
                                
                                if My_hedge.movement_needed[0] > 0.1:
                                        #Set direction for left movement
                                        Motor1.set_direction(0)
                                        Motor2.set_direction(1)
                                        Motor3.set_direction(1)
                                        Motor4.set_direction(0)
                                
                                elif (My_hedge.movement_needed[0] <0.1) AND (My_hedge.movement[0] > -0.1):
                                        #move ahead
                                        if My_hedge.movement_needed[1] > 0.1:
                                                #Set direction for forward movement
                                                Motor1.set_direction(0)
                                                Motor2.set_direction(0)
                                                Motor3.set_direction(0)
                                                Motor4.set_direction(0)
                                        elif (My_hedge.movement_needed[1] < 0.1) AND (My_hedge.movement_needed[1] > -0.1):
                                                #At position
                                                print('Destination acheived')
                                        else:
                                                #Set direction for backwards movement
                                                Motor1.set_direction(1)
                                                Motor2.set_direction(1)
                                                Motor3.set_direction(1)
                                                Motor4.set_direction(1)
                                        
                                else:
                                        #Set direction for right movement
                                        Motor1.set_direction(1)
                                        Motor2.set_direction(0)
                                        Motor3.set_direction(0)
                                        Motor4.set_direction(1)
                        
                        except KeyboardInterrupt:
                                hedge.stop()
                                sys.exit()
        except KeyboardInterrupt:
                hedge.stop()
                sys.exit()
                
main()


