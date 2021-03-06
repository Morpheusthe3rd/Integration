import RPi.GPIO as IO
import time
import datetime
import logging
import pygame
import math
import sys
import numpy

#From Online
# Setup pygame and key states
global hadEvent
global moveUp
global moveDown
global moveLeft
global moveRight
global moveQuit
global turnLeft
global turnRight
global upDown
global leftRight
upDown = 0
leftRight = 0
hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False
turnLeft = False
turnRight = False
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("JoyBorg - Press [ESC] to quit")
# From Online

axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 3                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time

# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global moveUp
    global moveDown
    global moveLeft
    global moveRight
    global moveQuit
    global upDown
    global leftRight
    # Handle each event individually
    for event in events:
        if event.type == pygame.QUIT:
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = True
        elif event.type == pygame.KEYUP:
            # A key has been released, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = False
        elif event.type == pygame.JOYAXISMOTION:
            # A joystick has been moved, read axis positions (-1 to +1)
            hadEvent = True
	    upDown_0 = upDown
	    leftRight_0 = leftRight
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            # Invert any axes which are incorrect
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
            # Determine Up / Down values
            if upDown < -0.1:
		if numpy.sign(upDown) != numpy.sign(upDown_0):
			all_accelerate(Power_a, Power_b, 0.01, 0, -1)
		upDown_2 = abs(upDown)
		upDown_2 = 75*upDown_2
		upDown_2 = int(upDown_2)
		print(upDown_2)
		if upDown > upDown_0:
	    		all_accelerate(Power_a, Power_b, 0.01, upDown, -1)
	    	all_accelerate(Power_a, Power_b, 0.01, upDown_2, 1)	
		moveUp = True
                moveDown = False
            elif upDown > 0.1:
		if numpy.sign(upDown) != numpy.sign(upDown_0):
			all_accelerate(Power_a, Power_b, 0.01, 0, -1)
		upDown = abs(upDown)
		upDown = 75*upDown
		upDown = int(upDown)
		print(upDown)
		if upDown < upDown_0:
	    		all_accelerate(Power_a, Power_b, 0.01, upDown, -1
		all_accelerate(Power_a, Power_b, 0.01, upDown, 1)
                moveUp = False
                moveDown = True
            else:
                moveUp = False
                moveDown = False
		all_accelerate(Power_a, Power_b, 0.01, 0, -1)
            # Determine Left / Right values
            if leftRight < -0.1:
		if numpy.sign(leftRight) != numpy.sign(leftRight_0):
			all_accelerate(Power_a, Power_b, 0.01, 0, -1)
		leftRight_2 = abs(leftRight)
		leftRight_2 = 75*leftRight_2
		leftRight_2 = int(leftRight_2)
		print(leftRight_2)
	    	all_accelerate(Power_a, Power_b, 0.01, leftRight_2, 1)		
                moveLeft = True
                moveRight = False
            elif leftRight > 0.1 :
		if numpy.sign(leftRight) != numpy.sign(leftRight_0):
			all_accelerate(Power_a, Power_b, 0.01, 0, -1)
		leftRight = abs(leftRight)
		leftRight = 75*leftRight
		leftRight = int(leftRight)
		print(leftRight)
	    	all_accelerate(Power_a, Power_b, 0.01, leftRight, 1)	
                moveLeft = False
                moveRight = True
            else:
                moveLeft = False
                moveRight = False
                

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

IO.setwarnings(False)
IO.setmode(IO.BCM)
logging.info('IO.setwarnings: False')
logging.info('IO.setmode: IO.BCM')

class Motor: #This class defines the motor direction pins and their assumed position on the robot. 
	def __init__(self, PIN_1, PIN_2):
		
		logging.debug('A motor has been initialized. It will be assumed to have no fixed position on the Robot until otherwise')
		logging.debug('assigned. The Motor class has 1 function, set_direction. This function allows the direction of motor movement')
		logging.debug('to be assigned. It alternates which GPIO pin has high voltage, thereby controling the direction. If both are')
		logging.debug('set to high, there will be no motion from the motor. It is assumed that the first Pin entered controlls forward')
		logging.debug('motion, and the second controls backward.')
		
		self.left = False
		self.right = False
		self.front = False
		self.back = False
		
		self.forward_pin = PIN_1
		self.backward_pin = PIN_2
		
		IO.setup(PIN_1,IO.OUT)
		IO.setup(PIN_2,IO.OUT)
		
	def set_direction(self, decision_bit):
		if decision_bit == 0:
			IO.output(self.forward_pin, IO.HIGH)
			IO.output(self.backward_pin, IO.LOW)
			logging.info('Direction Forward')
		elif decision_bit == 1:
			IO.output(self.forward_pin, IO.LOW)
			IO.output(self.backward_pin, IO.HIGH)
			logging.info('Direction Backward')
		else: 
			logging.warning("Exception. Unexpected 'decision_bit' value.")
class PWM: #This class defines the data and functions surrounding the PWM controls
	def __init__(self, PIN_1, Frequency):
		
		logging.debug('A PWM has just be instantiated. This class governs acceleration of the motors via a PWM signal. It has 1')
		logging.debug('function, Accelerate. This covers positive and negative acceleration, via a variable for loop.')
		
		self.output_Pin = PIN_1
		self.PWMFrequency = Frequency
		self.Current_duty_cycle = 0
		
		IO.setup(self.output_Pin, IO.OUT)
		self.MotorPWM = IO.PWM(self.output_Pin, self.PWMFrequency) #This section may not work as intended, look here first for errors.
		
	def Accelerate(self, final_duty_cycle, interval, direction):
	#The acceleration function handles both increases and decreases in duty cycle. This is possible through the range function, 
	#which allows the direction of the range to be set: 1 for upwards, -1 for reverse. The function iterates from the current
	#duty cycle to the final duty cycle, in the specified direction. It then sets the new current duty cycle to the desired one.
		logging.debug('Debug: accelerating')
		logging.debug('Final Duty Cycle: ') 
		logging.debug(final_duty_cycle)
		logging.debug('Interval: ' )
		logging.debug(interval)
		logging.debug('Direction: ')
		logging.debug(direction)
		for i in range (self.Current_duty_cycle, final_duty_cycle, direction):
			self.MotorPWM.ChangeDutyCycle(i)
			time.sleep(interval)
			logging.debug('PWM duty-cycle: %f', i)
		self.Current_duty_cycle = final_duty_cycle


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

Power_a.MotorPWM.start(0)
Power_b.MotorPWM.start(0)

def all_accelerate(PWM1, PWM2, interval, final_duty, direction):
	starting_duty = (PWM1.Current_duty_cycle + PWM2.Current_duty_cycle)/2
	for i in range (starting_duty, final_duty, direction):
		PWM1.MotorPWM.ChangeDutyCycle(i)
		PWM2.MotorPWM.ChangeDutyCycle(i)
		time.sleep(interval)
	PWM1.Current_duty_cycle = final_duty
	PWM2.Current_duty_cycle = final_duty

def main():
        global hadEvent
	hadEvent = False
        while(1):
                try:
                        #----------------TAKE INPUT----------------#
                    PygameHandler(pygame.event.get())
                    if hadEvent:
                    # Keys have changed, generate the command list based on keys
                        hadEvent = False
                        if moveQuit:
                            break
                        elif moveLeft:
                            Motor3.set_direction(1)
                            Motor2.set_direction(0)
                            Motor4.set_direction(0)
                            Motor1.set_direction(1)
                        elif moveRight:
                            Motor3.set_direction(0)
                            Motor2.set_direction(1)
                            Motor4.set_direction(1)
                            Motor1.set_direction(0)
                        elif moveUp:
                            Motor3.set_direction(1)
                            Motor2.set_direction(1)
                            Motor4.set_direction(1)
                            Motor1.set_direction(1)        
                        elif moveDown:
                            Motor3.set_direction(0)
                            Motor2.set_direction(0)
                            Motor4.set_direction(0)
                            Motor1.set_direction(0)
                    # Wait for the interval period
                    time.sleep(0.01)
                except KeyboardInterrupt:
                        logging.warning('KEYBOARD INTERRUPT. PROGRAM EXITING.')
                        sys.exit()
                        break
                        


main()

