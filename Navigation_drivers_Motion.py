import time
from navigation_drivers_MM_interpreter_mk1 import hedge_Positions
from motordrivers_mk2 import Motor
from motordrivers_mk2 import PWM
from marvelmind import MarvelmindHedge
import sys
import Fundamentals

#This file plans to take the input from the Marvelmind beacons and the interpreter, and act on the movement recommendations from that
#interpreter. 

#Assume that the robot is properly oriented

def main():
        
        hedge = MarvelmindHedge(tty = "/dev/ttyACM0",adr=9, debug=False)
        hedge.start()
        My_hedge = hedge_Positions()
        
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
        
        #Current direction flags. These will determine wether or not the robot needs to decelerate before changing directions
        Left_dir_flag = False
        Right_dir_flag = False
        Back_dir_flag = False
        Front_dir_flag = False
        
        #PWM wave setup
        PWM_a = PWM(18,100)
        PWM_b = PWM(13,100)
        
        try:
                while True:
                        try:
                                My_hedge.update_position()
                                #IF direction 
                                if My_hedge.Movement_needed[0] > 0.1:
                                        if Left_dir_flag == False:
                                                
                                                #all decelerate
                                                PMW_a.Accelerate(0, 0.05, -1)
                                                PWM_b.Accelerate(0, 0.05, -1)
                                                                                               
                                                #Set direction for left movement
                                                Motor1.set_direction(0)
                                                Motor2.set_direction(1)
                                                Motor3.set_direction(1)
                                                Motor4.set_direction(0)
                                                Left_dir_flag = True
                                                
                                                #all accelerate
                                                PMW_a.Accelerate(50, 0.05, 1)
                                                PWM_b.Accelerate(50, 0.05, 1)
                                                
                                elif (My_hedge.Movement_needed[0] <0.1) and (My_hedge.Movement[0] > -0.1):
                                        #move ahead
                                        if My_hedge.Movement_needed[1] > 0.1:
                                                if Front_dir_flag == False:
                                                        
                                                        #all decelerate
                                                        PMW_a.Accelerate(0, 0.05, -1)
                                                        PWM_b.Accelerate(0, 0.05, -1)
                                                        
                                                        #Set direction for forward movement
                                                        Motor1.set_direction(0)
                                                        Motor2.set_direction(0)
                                                        Motor3.set_direction(0)
                                                        Motor4.set_direction(0)
                                                        Front_dir_flag = True
                                                        
                                                        #all accelerate
                                                        PMW_a.Accelerate(50, 0.05, 1)
                                                        PWM_b.Accelerate(50, 0.05, 1)
                                                        
                                        elif (My_hedge.Movement_needed[1] < 0.1) and (My_hedge.Movement_needed[1] > -0.1):
                                                #At position
                                                print('Destination acheived')
                                                #all decelerate
                                        else:
                                                if Back_dir_flag == False:
                                                        
                                                        #all decelerate
                                                        PMW_a.Accelerate(0, 0.05, -1)
                                                        PWM_b.Accelerate(0, 0.05, -1)
                                                        
                                                        #Set direction for backwards movement
                                                        Motor1.set_direction(1)
                                                        Motor2.set_direction(1)
                                                        Motor3.set_direction(1)
                                                        Motor4.set_direction(1)
                                                        Back_dir_flag = True
                                                        
                                                        #all accelerate
                                                        PMW_a.Accelerate(50, 0.05, 1)
                                                        PWM_b.Accelerate(50, 0.05, 1)
                                                        
                                else:
                                        if Right_dir_flag == False:
                                                
                                                #all decelerate
                                                PMW_a.Accelerate(0, 0.05, -1)
                                                PWM_b.Accelerate(0, 0.05, -1)
                                                
                                                #Set direction for right movement
                                                Motor1.set_direction(1)
                                                Motor2.set_direction(0)
                                                Motor3.set_direction(0)
                                                Motor4.set_direction(1)
                                                Right_dir_flag = True
                                                
                                                #all accelerate
                                                PMW_a.Accelerate(50, 0.05, 1)
                                                PWM_b.Accelerate(50, 0.05, 1)
                                                        
                                time.sleep(1)
                                
                        except KeyboardInterrupt:
                                hedge.stop()
                                sys.exit()
        except KeyboardInterrupt:
                hedge.stop()
                sys.exit()
                
main()


