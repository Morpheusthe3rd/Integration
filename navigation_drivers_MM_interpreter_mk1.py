import time
from marvelmind import MarvelmindHedge
import math
import sys

#This file is set up to take in the data from the marvelmind network and transform
#that into a movement recommendation. Actuall implementation of the recommendations will
#be executed by a seperate driver

hedge = MarvelmindHedge(tty = "/dev/ttyACM0",adr=9, debug=False)
hedge.start()

class hedge_Positions:	#This class contains the data on the hedgehog positions, and the method to update them.
	def __init__(self):
		self.Position_now = [hedge.position()[1], hedge.position()[2]]
		self.Position_minus1 = [0, 0]
		self.Position_minus2 = [0, 0]
		self.Target_coord = [0, 0]
		self.Target_coord[0] = input('Please enter target location X coord.: ')
		self.Target_coord[1] = input('Please enter target location Y coord.: ')
		print ('Target: ',self.Target_coord)
		self.Movement_needed = [0, 0]
		
	def update_position(self):
		self.Position_minus2 = self.Position_minus1
		self.Position_minus1 = self.Position_now
		self.Position_now[0] = hedge.position()[1]
		self.Position_now[1] = hedge.position()[2]
		
		self.Movement_needed[0] = self.Target_coord[0] - self.Position_now[0]
		self.Movement_needed[1] = self.Target_coord[1] - self.Position_now[1]

class Impassable_zone: #This class defines a zone on the map which our system is unable to pass through, such as a table or a wall. 
		       #It uses the x/y coordinates to define this zone, but therefore can only accept rectangles. 
	def __init__(self, X1, X2, Y1, Y2):
		self.X1 = X1
		self.X2 = X2
		self.Y1 = Y1
		self.Y2 = Y2
		
class motion_path: #This class defines a zone of the map which our system is encourgaged to pass through. 
	def __init__(self, X1, X2, Y1, Y2):
		self.X1 = X1
		self.X2 = X2
		self.Y1 = Y1
		self.Y2 = Y2
		
def print_all():
	print('Postition now: ')
	print(Position_now)
	print('Position 1 reading ago: ')
	print(Position_minus1)
	print('Position 2 readings ago: ')
	print(Position_minus2)

def main():
	#global hedge
	#print_all() #attempt to print all

	My_hedge = hedge_Positions()
	
	#print('Welcome to navigation_drivers_MM_interpreter_mk.1!.')
	#My_hedge.Target_coord[0] = input('Please enter target location X coord.: ')
	#My_hedge.Target_coord[1] = input('Please enter target location Y coord.: ')
	#print ('Target: ',My_hedge.Target_coord)

	while True:
		try:
			My_hedge.update_position()

			#My_hedge.Movement_needed[0] = My_hedge.Target_coord[0] - My_hedge.Position_now[1]
			#My_hedge.Movement_needed[1] = My_hedge.Target_coord[1] - My_hedge.Position_now[1]

			print('Movement needed: x=%.3f, y=%.3f' % (My_hedge.Movement_needed[0],My_hedge.Movement_needed[1]))
			time.sleep(1)

		except KeyboardInterrupt:
			hedge.stop()
			sys.exit()

main()
