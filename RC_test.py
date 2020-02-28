import RPi.GPIO as IO
import time
import datetime
import logging

logging.basicConfig(filename='Motordriver.log', level=logging.DEBUG) 
logging.info('Logging file begin. Date of most recent run: %s', datetime.datetime.now())

logging.info('Imported packages:')
logging.info('		RPi.GPIO as IO')
logging.info('		time')
logging.info('		datetime')
logging.info('		logging')

#This file is the preliminary interface test for the MIT AI2 app which will control our robot. This model will simply print the text 
#which comes from the App

main():
        while(1):
                try:
                        #----------------TAKE INPUT----------------#
                        Input_string = #input
                        print(Input_string)
                except KeyboardInterupt:
                        logging.warning('KEYBOARD INTERRUPT. PROGRAM EXITING.')
                        sys.exit()
                        break
                        
                        
