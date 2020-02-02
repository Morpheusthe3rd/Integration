import time
from marvelmind import MarvelmindHedge
import math
import sys

#This file is set up to take in the data from the marvelmind network and transform
#that into a movement recommendation. Actuall implementation of the recommendations will
#be executed by a seperate driver

Position_now = [0, 0]
Position_minus1 = [0, 0]
Position_minus2 = [0, 0]
Target_coord = [0, 0]

Movement_needed = [0, 0]

hedge = MarvelmindHedge(tty = "/dev/ttyACM0",adr=9, debug=False)
hedge.start()

def get_current_pos():
	global Position_minus1
	global Position_minus2
	global Position_now
	global hedge
	Position_minus2 = Position_minus1
	Position_minus1 = Position_now
	Position_now = hedge.position()

def print_all():
	print('pos_now:',Position_now)
	print('pos_minus1: ',Position_minus1)
	print('pos_minus2: ',Position_minus2)

def main():
	#global hedge
	print_all() #attempt to print all

	print('Welcome to navigation_drivers_MM_interpreter_mk.1!.')
	Target_coord[0] = input('Please enter target location X coord.: ')
	Target_coord[1] = input('Please enter target location Y coord.: ')
	print ('Target: ',Target_coord)

	while True:
		try:
			get_current_pos()
	 	#	Position_now = hedge.position()
		#	print(Position_now)
			Movement_needed[0] = Target_coord[0] - Position_now[1]
			Movement_needed[1] = Target_coord[1] - Position_now[2]

			

			print('Movement needed: x=%.3f, y=%.3f' % (Movement_needed[0],Movement_needed[1]))
			#hedge.print_position()
			time.sleep(1)

		except KeyboardInterrupt:
			hedge.stop()
			sys.exit()
main()
