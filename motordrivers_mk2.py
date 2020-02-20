import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

class Motor: #This lass defines the motor direction pins and their assumed position on the robot. 
	def __init__(self, PIN_1, PIN_2):
		
		self.left = False
		self.right = False
		self.front = False
		self.back = False
		
		self.forward_pin = PIN_1
		self.backward_pin = PIN_2
		
		IO.setup(PIN_1,IO.OUT)
		IO.setup(PIN_2,IO.OUT)
		
	def set_direction(decision_bit)
		if decision_bit == 0:
			IO.output(self.forward_pin, IO.HIGH)
			IO.output(self.backward_pin, IO.LOW)
		elif decision_bit == 1:
			IO.output(self.forward_pin, IO.LOW)
			IO.output(self.backward_pin, IO.HIGH)
		else: 
			print("Exception. Unexpected 'decision_bit' value.")

#PWM manager pins
IO.setup(18,IO.OUT) #right side
IO.setup(13,IO.OUT) #left side

#Motor 1 pins (assumed front right)
Motor1 = Motor(17, 27)

#Motor 2 pins (assumed back right)
Motor2 = Motor(22,23)

#Motor 3 pins (assumed front left)
Motor3 = Motor(24,25)

#Motor 4 pins (assumed back left)
Motor4 = Motor(5,6)

#PWM wave setup
PWM_a = IO.PWM(18, 100)
PWM_b = IO.PWM(13, 100)

#PWM test-
#This function allows testing of a single PWM. The signal should
#increase to 100% Duty-cycle, then decrease. The full process should
#complete in 2 seconds
def PWM_a_test():

	print('Start PWM_a test')
	PWM_a.start(0) #Starts PWM_a with a 0% duty cycle
	for x in range(100): #Duty cycle increases by 1% every hundredth
			     #of a second
		PWM_a.ChangeDutyCycle(x)
		time.sleep(0.05)
	for x in range(100):
		PWM_a.ChangeDutyCycle(100-x)
		time.sleep(0.05)
	print('End PWM_a test')

#Motor control setup-
#These functions are the building blocks of the robot's motion. They are
#divided into acceleration, decelleration, and direction sections.


#This function causes both PWM's to accelerate. The 'X' input defines the
#wait period between interations, and 'Y' defines max PWM duty cycle
def Motor_control_accelerate_all(X,Y):


	PWM_a.start(0)
	PWM_b.start(0)

	for i in range(Y):
		PWM_a.ChangeDutyCycle(i)
		PWM_b.ChangeDutyCycle(i)
		time.sleep(X)


#This function causes both PWM's to decelerate. The 'X' input defines the
#wait period between interations, and 'Y' defines max PWM duty cycle
def Motor_control_decelerate_all(X,Y):

	
        PWM_a.start(0)
        PWM_b.start(0)

        for i in range(Y):
                PWM_a.ChangeDutyCycle(100-i)
                PWM_b.ChangeDutyCycle(100-i)
                time.sleep(X)
	

#This function causes PWM_a to accelerate. The 'X' input defines the 
#wait period between interations, and 'Y' defines max PWM duty cycle
def Motor_control_accelerate_a(X,Y):

	
        PWM_a.start(0)
        for i in range(Y):
                PWM_a.ChangeDutyCycle(i)
                time.sleep(X)
	
#This function causes PWM_a to decelerate. The 'X' input defines the 
#wait period between interations, and 'Y' defines max PWM duty cycle
def Motor_control_decelerate_a(X,Y):
        PWM_a.start(0)

        for i in range(Y):
                PWM_a.ChangeDutyCycle(100-i)
                time.sleep(X)

#This function causes PWM_b to accelerate. The 'X' input defines the 
#wait period between interations, and 'Y' defines max PWM duty cycle
def Motor_control_accelerate_b(X,Y):
        PWM_b.start(0)

        for i in range(Y):
                PWM_b.ChangeDutyCycle(i)
                time.sleep(X)

#This function causes PWM_b to decelerate. The 'X' input defines the 
#wait period between interations, and 'Y' defines max PWM duty cycle
def Motor_control_decelerate_b(X,Y):
        PWM_b.start(0)

        for i in range(Y):
                PWM_b.ChangeDutyCycle(100-i)
                time.sleep(X)

#This function should be appended to the end of all programs operating motors
#It sets all of the motor direction controls to stationary

def All_stop():
	IO.output(17,IO.LOW)
	IO.output(27,IO.LOW)
	IO.output(22,IO.LOW)
	IO.output(23,IO.LOW)
	IO.output(24,IO.LOW)
	IO.output(25,IO.LOW)
	IO.output(5,IO.LOW)
	IO.output(6,IO.LOW)

	PWM_a.stop()
	PWM_b.stop()
	print('All motors should now be stopped')

#Main function-
#The main function in this particular function is just going to be a demo, essentially
#running through all the various operations our drive system is capable of.
def main():
	print('Main start.')

	#Operation 0: PWM_test
	PWM_a_test()

	#Operation 1: all motors forward, accelerate, 1 sec pause, decelerate
	print('Start operation 1, all motors forward, accelerate, pause, decelerate.')
	Motor1.set_direction(0)
	Motor2.set_direction(0)
	Motor3.set_direction(0)
	Motor4.set_direction(0)

	Motor_control_accelerate_all(0.05,25)
	time.sleep(2)
	Motor_control_decelerate_all(0.05,25)
	print('End operation 1.')

	#Operation 2: all motors backwards, accelerate, 1 sec pause, decelerate
	print('Start operation 2, all motors back, accelerate, pause, decelerate.')
        Motor1.set_direction(1)
        Motor2.set_direction(1)
        Motor3.set_direction(1)
        Motor4.set_direction(1)

        Motor_control_accelerate_all(0.05,25)
        time.sleep(2)
        Motor_control_decelerate_all(0.05,25)
	print('End operation 2.')

	#Operation 3: Tank turn. Left forward, right back, accelerate, 1 sec pause,
	#decelerate
	print('Start operation 3, left forward, right back, accelerate, pause decelerate.')
        Motor1.set_direction(1)
        Motor2.set_direction(1)
        Motor3.set_direction(0)
        Motor4.set_direction(0)

        Motor_control_accelerate_all(0.05,25)
        time.sleep(2)
        Motor_control_decelerate_all(0.05,25)
	print('End operation 3.')
	#Operation 4: Crab. Front backwards, back forwards, accelerate, 1 sec pause,
	#decelerate
	print('Start operation 4, front backwards, back frontwards, accelerate, pause, decelerate')
        Motor1.set_direction(0)
        Motor2.set_direction(1)
        Motor3.set_direction(0)
        Motor4.set_direction(1)

        Motor_control_accelerate_all(0.05,25)
        time.sleep(2)
        Motor_control_decelerate_all(0.05,25)
	print('End operation 4.')

	#Operation 5: All motors stop
	print('Start operation 5, all stop.')
	All_stop()
	print('End operation 5.')

main()
	
