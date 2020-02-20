import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

class Motor: #This class defines the motor direction pins and their assumed position on the robot. 
	def __init__(self, PIN_1, PIN_2):
		
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
			print('Direction Forward')
		elif decision_bit == 1:
			IO.output(self.forward_pin, IO.LOW)
			IO.output(self.backward_pin, IO.HIGH)
			print('Direction Backward')
		else: 
			print("Exception. Unexpected 'decision_bit' value.")
class PWM: #This class defines the data and functions surrounding the PWM controls
	def __init__(self, PIN_1, Frequency):
		
		self.output_Pin = PIN_1
		self.Frequency = Frequency
		self.Current_duty_cycle = 0
		
		IO.setup(PIN_1, IO.OUT)
		self.PWM = IO.PWM(PIN_1, Frequency) #This section may not work as intended, look here first for errors.
		
	def Accelerate(self, final_duty_cycle, interval, direction):
	#The acceleration function handles both increases and decreases in duty cycle. This is possible through the range function, 
	#which allows the direction of the range to be set: 1 for upwards, -1 for reverse. The function iterates from the current
	#duty cycle to the final duty cycle, in the specified direction. It then sets the new current duty cycle to the desired one.
		print('Debug: accelerating')
		print('Final Duty Cycle: ') 
		print(final_duty_cycle)
		print('Interval: ' )
		print(interval)
		print('Direction: ')
		print(direction)
		for i in range (self.Current_duty_cycle, final_duty_cycle, direction):
			self.PWM.ChangeDutyCycle(i)
			time.sleep(interval)
			#print(i)
		self.Current_duty_cycle = final_duty_cycle


#Motor 1 pins (assumed front right)
Motor1 = Motor(17, 27)

#Motor 2 pins (assumed back right)
Motor2 = Motor(22,23)

#Motor 3 pins (assumed front left)
Motor3 = Motor(24,25)

#Motor 4 pins (assumed back left)
Motor4 = Motor(5,6)

#PWM wave setup
Power_a = PWM(18,100)
Power_b = PWM(13,100)

#PWM test-
#This function allows testing of a single PWM. The signal should
#increase to 100% Duty-cycle, then decrease. The full process should
#complete in 2 seconds
def PWM_a_test():

	print('Start PWM_a test')
	PWM_a.PWM.start(0) #Starts PWM_a with a 0% duty cycle
	PWM_a.Accelerate(100, 0.01, 1)
	PWM_a.Accelerate(0, 0.01, -1)
	print('End PWM_a test')

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
	IO.output(18,IO.LOW)
	IO.output(13,IO.LOW)
	print('All motors should now be stopped')

#Main function-
#The main function in this particular function is just going to be a demo, essentially
#running through all the various operations our drive system is capable of.
def main():
	print('Main start.')

	#Operation 0: PWM_test
	#PWM_a_test()

	#Operation 1: all motors forward, accelerate, 1 sec pause, decelerate
	print('Start operation 1, all motors forward, accelerate, pause, decelerate.')
	Motor1.set_direction(0)
	Motor2.set_direction(0)
	Motor3.set_direction(0)
	Motor4.set_direction(0)

	Power_a.Accelerate(50, 0.01, 1)
	Power_b.Accelerate(50, 0.01, 1)
	
	time.sleep(2)
	
	Power_a.Accelerate(50, 0.01, -1)
	Power_b.Accelerate(50, 0.01, -1)
	
	
	print('End operation 1.')

	#Operation 2: all motors backwards, accelerate, 1 sec pause, decelerate
	print('Start operation 2, all motors back, accelerate, pause, decelerate.')
        Motor1.set_direction(1)
        Motor2.set_direction(1)
        Motor3.set_direction(1)
        Motor4.set_direction(1)

	Power_a.Accelerate(50, 0.01, 1)
	Power_b.Accelerate(50, 0.01, 1)
	
	time.sleep(2)
	
	Power_a.Accelerate(50, 0.01, -1)
	Power_b.Accelerate(50, 0.01, -1)
	print('End operation 2.')

	#Operation 3: Tank turn. Left forward, right back, accelerate, 1 sec pause,
	#decelerate
	print('Start operation 3, left forward, right back, accelerate, pause decelerate.')
        Motor1.set_direction(1)
        Motor2.set_direction(1)
        Motor3.set_direction(0)
        Motor4.set_direction(0)

	Power_a.Accelerate(50, 0.01, 1)
	Power_b.Accelerate(50, 0.01, 1)
	
	time.sleep(2)
	
	Power_a.Accelerate(50, 0.01, -1)
	Power_b.Accelerate(50, 0.01, -1)
	print('End operation 3.')
	
	#Operation 4: Crab. Front backwards, back forwards, accelerate, 1 sec pause,
	#decelerate
	print('Start operation 4, front backwards, back frontwards, accelerate, pause, decelerate')
        Motor1.set_direction(0)
        Motor2.set_direction(1)
        Motor3.set_direction(0)
        Motor4.set_direction(1)

	Power_a.Accelerate(50, 0.01, 1)
	Power_b.Accelerate(50, 0.01, 1)
	
	time.sleep(2)
	
	Power_a.Accelerate(50, 0.01, -1)
	Power_b.Accelerate(50, 0.01, -1)
	print('End operation 4.')

	#Operation 5: All motors stop
	print('Start operation 5, all stop.')
	All_stop()
	print('End operation 5.')


main()
