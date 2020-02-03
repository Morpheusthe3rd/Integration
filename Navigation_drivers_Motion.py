import time
import navigation_drivers_MM_interpreter_mk1
import motordrivers_mk2
import marvelmind
import sys

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
                                
                                if My_hedge.movement_needed[0] > 0:
                                        #move left
                                
                                elif My_hedge.movement_needed[0] == 0:
                                        #move ahead
                                
                                else:
                                        #move right
                        
                        except KeyboardInterrupt:
                                hedge.stop()
                                sys.exit()
        except KeyboardInterrupt:
                hedge.stop()
                sys.exit()
                
main()


