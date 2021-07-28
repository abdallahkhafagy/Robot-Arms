import RPi.GPIO as GPIO  
from time import sleep      
GPIO.setmode(GPIO.BCM)       
GPIO.setup(17, GPIO.IN)    
  
try:  
    while True:              
        if not GPIO.input(17):   
            print ("object detected")  
        else:  
            print ("object free") 
        sleep(0.1)         
  
finally:                   
    GPIO.cleanup()           
