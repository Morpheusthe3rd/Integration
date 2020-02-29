import time
import sys
import marvelmind

#This test program will test whether or not I can nab opponents hedgehog 
#address from the system

def main():

	try:
		hedge_enemy = 100

		hedgeX = marvelmind.MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False)
		hedgeX.start()

		hedge_self = 9

		hedge_readings = [9, 9]
		while len(hedge_readings)<40:
			time.sleep(0.1)
			print('mark')
			try:
				for i in range (4):
					hedge_readings.append(hedgeX.position()[0])
					time.sleep(0.01)

				print(hedge_readings)

			except KeyboardInterrupt:
				hedgeX.stop()
				sys.exit()
				
		for i in range (len(hedge_readings)):
			if hedge_readings[i] == 9:
				hedge_readings[i] = 0
			else:
				hedge_enemy = hedge_readings[i]
			
		print(hedge_enemy)
			
	except KeyboardInterrupt:
		hedgeX.stop()
		sys.exit()
main()
