# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:49:39 2021

@author: Abdullah
"""


from UpperBody import UpperBody
import time

upper = UpperBody()

time.sleep(3)
upper.runScenario("Scenario04")



'''
time.sleep(2)
upper.runScenario("Scenario01")
time.sleep(5)
upper.runScenario("Scenario02")
time.sleep(5)
'''
#upper.runScenario("Scenario03")



from Hand import Hand
from Shoulder import Shoulder
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
MAX_ANG  =[10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#MAX_ANG  =[150, 140, 140, 150, 120, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
MIN_ANG=[180, 180, 180, 180, 180,  170,  50, 180, 130, 120, 155, 175, 100]
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]

MIN_ANGS = [40, 180,   180]
MAX_ANGS  =[180, 0, 0]
driver = ServoKit(channels=16,address = 0x42)
#RHand = Hand(driver,[0,1,2,3,4],MAX_ANG,MIN_ANG,MIN_IMP,MAX_IMP,"")
#RHand.openHand()
#RShoulder = Shoulder(driver,[6,7,8],MAX_ANGS,MIN_ANGS,MIN_IMP,MAX_IMP,"")
#driver.servo[5].angle = 180
'''
#Constants
nbPCAServo=5
servoValues = [0,0,0,0,0]
#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MAX_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#MAX_ANG  =[150, 140, 140, 150, 120, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
MIN_ANG=[160, 160, 160, 160, 160,  170,  50, 180, 130, 120, 155, 175, 100]

MIN_ANGS = [40, 180,   180]
MAX_ANGS  =[180, 0, 0]
'''
#driver = ServoKit(channels=16,address = 0x42)
#driver.servo[0].angle = 160
#driver.servo[5].angle = 160
'''driver.servo[7].angle = 0

#driver.servo[7].angle = 0
RShoulder.ReleaseAll()
time.sleep(3)
RShoulder.setAngle(0,0)
RShoulder.setAngle(1,0)
'''
'''
RShoulder = Shoulder(driver,[6,7,8],MAX_ANGS,MIN_ANGS,MIN_IMP,MAX_IMP)
RHand = Hand(driver,[0,1,2,3,4,5],MAX_ANG,MIN_ANG,MIN_IMP,MAX_IMP)
'''
# 0 - 180
# 2 - 120
'''
RShoulder.setAngle(0,1)
RShoulder.setAngle(1,1)
RShoulder.setAngle(2,1)

RHand.closeHand()
time.sleep(3)

RShoulder.setAngle(0,130)
RShoulder.setAngle(1,180)
RShoulder.setAngle(2,100)

time.sleep(2)

RHand.openHand()
RHand.setAngle(5,60)

for i in range(0,3):
    for i in range(80,130,5):
        driver.servo[9].angle = i #80-130
        time.sleep(0.1)

    for i in range(130,80,-5):
        driver.servo[9].angle = i #80-130
        time.sleep(0.1)

time.sleep(2)

RHand.closeHand()
'''

'''
RShoulder.setAngle(0,100)
RShoulder.setAngle(1,100)
RShoulder.setAngle(2,1)
RHand.openHand()


time.sleep(2)
RShoulder.setAngle(0,0)
RShoulder.setAngle(1,100)

time.sleep(2)
RShoulder.setAngle(0,0)
RShoulder.setAngle(1,0)

time.sleep(2)
RShoulder.setAngle(0,0)
RShoulder.setAngle(1,180)

time.sleep(2)
RShoulder.setAngle(0,0)
RShoulder.setAngle(1,0)

#RShoulder.setAngle(2,120)
time.sleep(2)

RHand.closeHand()
time.sleep(2)

RHand.openHand()
'''

'''
RShoulder = Shoulder(driver,[6,7,8],MAX_ANGS,MIN_ANGS,MIN_IMP,MAX_IMP)

RShoulder.ReleaseAll()
time.sleep(3)

driver.servo[0].angle = 160
driver.servo[1].angle = 160
driver.servo[2].angle = 150
driver.servo[3].angle = 160
driver.servo[4].angle = 150
time.sleep(10)


RShoulder.setAngle(0,180)
RShoulder.setAngle(2,120)
time.sleep(3)

driver.servo[0].angle = 0
driver.servo[1].angle = 0
driver.servo[2].angle = 0
driver.servo[3].angle = 0
driver.servo[4].angle = 0
driver.servo[4].angle = 160

time.sleep(5)
RShoulder.setAngle(1,0)
RShoulder.setAngle(2,20)
'''
'''
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)    #SO1
GPIO.output(4, GPIO.LOW)
driver.servo[6].angle = 170




time.sleep(10)
GPIO.output(4, GPIO.HIGH)

driver.servo[6].angle = 0
while True:

    l = 120
    for i in range(0,100):
        driver.servo[7].angle = i*90/100
        time.sleep(0.01)

    time.sleep(1)
    for i in range(100,0,-1):
        driver.servo[7].angle = i*90/100
        time.sleep(0.01)

'''
