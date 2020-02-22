import sys
import time

#This file contains all of the basic functions which might be used in any of the other files or functions

#The debug function should be plugged in almost every statement that performs an operation. It's inputs are the debug message and the 
#log level. This is basically to allow me to not have to rewrite the if else statements a thousand times. 
def debug(X, Y):
        if Y == 'debug':
                f1=open('./logs', 'w+')
                f1.write(X)
                f1.close()
                
def warning(X,Y):
        if Y == 'warning':
                f1=open('./logs', 'w+')
                f1.write(X)
                f1.close()
                
def error(X,Y):
        if Y == 'error':
                f1=open('./logs', 'w+')
                f1.write(X)
                f1.close()                
