import RPi.GPIO as IO
import time
import datetime
import logging
from motordrivers_mk2 import Motor
from motordrivers_mk2 import PWM


logging.basicConfig(filename='RC_TEST.log', level=logging.DEBUG) 
logging.info('Logging file begin. Date of most recent run: %s', datetime.datetime.now())

logging.info('Imported packages:')
logging.info('		RPi.GPIO as IO')
logging.info('		time')
logging.info('		datetime')
logging.info('		logging')

#This file is the preliminary interface test for the MIT AI2 app which will control our robot. This model will simply print the text 
#which comes from the App

#For now I will assume that the keyboard will be controlling the movement, using W, A, S, D

#Motor 3 pins (assumed front right)
Motor3 = Motor(17, 27)

#Motor 2 pins (assumed back right)
Motor2 = Motor(22,23)

#Motor 4 pins (assumed front left)
Motor4 = Motor(24,25)

#Motor 1 pins (assumed back left)
Motor1 = Motor(5,6)

#PWM wave setup
Power_a = PWM(18,100)
Power_b = PWM(13,100)

def all_accelerate(PWM1, PWM2, interval, final_duty, direction):
	starting_duty = (PWM1.Current_duty_cycle + PWM2.Current_duty_cycle)/2
	for i in range (starting_duty, final_duty, direction):
		PWM1.MotorPWM.ChangeDutyCycle(i)
		PWM2.MotorPWM.ChangeDutyCycle(i)
		time.sleep(interval)
	PWM1.Current_duty_cycle = final_duty
	PWM2.Current_duty_cycle = final_duty

main():
        Input_string0 = ''
        while(1):
                try:
                        #----------------TAKE INPUT----------------#
                        Input_string1 = Input_string0
                        Input_string0 = raw_input('')
                        print(Input_string0)
                        if Input_string0 == 'a':
                                #detect if direction is the same
                                if Input_string1 == Input_string0:
                                        #do nothing
                                else:
                                        #all decelerate, switch directions, accelerate
                                        all_accelerate(Power_a, Power_b, 0.01, 0 -1)
                                        #set direction for left movement
                                        Motor3.set_direction(1)
                                        Motor2.set_direction(0)
                                        Motor4.set_direction(0)
                                        Motor1.set_direction(1)
                                        all_accelerate(Power_a, Power_b, 0.01, 50, 1)
                        else if Input_string0 == 'w':
                                #detect if direction is the same
                                if Input_string1 == Input_string0:
                                        #do nothing
                                else:
                                        #all decelerate, switch directions, accelerate
                                        all_accelerate(Power_a, Power_b, 0.01, 0 -1)
                                        Motor3.set_direction(1)
                                        Motor2.set_direction(1)
                                        Motor4.set_direction(1)
                                        Motor1.set_direction(1)
                                        all_accelerate(Power_a, Power_b, 0.01, 50, 1)
                                #set direction for forward movement
                        else if Input_string0 == 's':
                                #detect if direction is the same
                                if Input_string1 == Input_string0:
                                        #do nothing
                                else:
                                        #all decelerate, switch directions, accelerate
                                        all_accelerate(Power_a, Power_b, 0.01, 0 -1)
                                        Motor3.set_direction(0)
                                        Motor2.set_direction(0)
                                        Motor4.set_direction(0)
                                        Motor1.set_direction(0)
                                        all_accelerate(Power_a, Power_b, 0.01, 50, 1)
                                #set direction for back movement
                        else if Input_string0 == 'd':
                                #detect if direction is the same
                                if Input_string1 == Input_string0:
                                        #do nothing
                                else:
                                        #all decelerate, switch directions, accelerate
                                        all_accelerate(Power_a, Power_b, 0.01, 0 -1)
                                        Motor3.set_direction(0)
                                        Motor2.set_direction(1)
                                        Motor4.set_direction(1)
                                        Motor1.set_direction(0)
                                        all_accelerate(Power_a, Power_b, 0.01, 50, 1)
                                #set direction for right movement
                        else:
                                #this is an error case.
                except KeyboardInterupt:
                        logging.warning('KEYBOARD INTERRUPT. PROGRAM EXITING.')
                        sys.exit()
                        break
                        
                        
