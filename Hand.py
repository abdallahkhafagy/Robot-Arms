# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:54:39 2021

@author: Abdullah
"""
from Servo_system import Servo_system
import time
class Hand(Servo_system):

  def __init__(self,driver, index_list,initial_angles, max_angle,min_angle,MIN_IMP,MAX_IMP,path):
      super().__init__( driver,index_list,initial_angles, max_angle,min_angle,MIN_IMP,MAX_IMP,path)






    # function testfingure
  def closeHand(self):
      """Scenario to test servo"""

      for j in range(0,int(101),1):
          print("MAX Angle",self.MAX_ANG)



          for finger in range(0,len(self.Servo_list),1):
              #print(finger)
              self.Servo_list[finger].setAngle(self.Servo_list[finger].angle_max*j/100)
              print(int(self.MAX_ANG[finger]*j/100))
              #self.servoValues[fingure] =self.Servo_list[fingure].getAngle()
          #pca.servo[fingure].angle = j
          time.sleep(0.001)


      time.sleep(0.001)




    # function testfingure
  def openHand(self):
      """Scenario to test servo"""

      for j in range(0,int(101),1):




          for finger in range(0,len(self.Servo_list),1):
              self.Servo_list[finger].setAngle(int(self.Servo_list[finger].angle_min*j/100))
              print(int(self.MIN_ANG[finger]*j/100))
              #self.servoValues[fingure] =self.Servo_list[fingure].getAngle()
          #pca.servo[fingure].angle = j
          time.sleep(0.001)


      time.sleep(0.001)




    # function testfingure
  def NaiveopenHand(self):
      """Scenario to test servo"""

      for i in range(0,len(self.Servo_list),1):

          self.Servo_list[i].setAngle(self.Servo_list[i].angle_min)
          print("yoooooh",self.Servo_list[i].angle_min)






          time.sleep(0.001)
      for i in range(0,len(self.Servo_list),1):
          self.Servo_list[i].setAngle(None) #disable channel

      time.sleep(0.001)


    # function testfingure
  def closeHand_f(self,fingures):
      """Scenario to test servo"""

      for j in range(0,int(101),1):



          for fingure in range(0,len(self.servo_list),1):
              self.servo_list[fingure].setAngle(int(self.MAX_ANG[fingure]*j/100) *fingures[fingure])
              self.servoValues[fingure] =self.servo_list[fingure].getAngle()
          #pca.servo[fingure].angle = j
          time.sleep(0.001)
      for i in range(0,len(self.servo_list),1):
          self.servo_list[fingure].setAngle(None) #disable channel

      time.sleep(0.001)

    # function testfingure
  def closeHand_h(self,fingures):
      """Scenario to test servo"""

      for j in range(0,int(101),1):



          for fingure in range(0,len(self.servo_list),1):
              self.servo_list[fingure].setAngle(int(self.MAX_ANG[fingure]*j/100) *fingures[fingure])
              self.servoValues[fingure] =self.servo_list[fingure].getAngle()
          #pca.servo[fingure].angle = j
          time.sleep(0.001)
      for i in range(0,len(self.servo_list),1):
          self.servo_list[fingure].setAngle(None) #disable channel

      time.sleep(0.001)



    # function testfingure
  def close(self,fingure):


      """Scenario to test servo"""
      for j in range(self.MIN_ANG[fingure],self.MAX_ANG[fingure],1):
          print("Send angle {} to Servo {}".format(j,fingure))
          #self.pca.servo[fingure].angle = j
          self.servoValues[fingure] = j #self.pca.servo[fingure].angle
          time.sleep(0.001)
      for j in range(self.MAX_ANG[fingure],self.MIN_ANG[fingure],-1):
          print("Send angle {} to Servo {}".format(j,fingure))
          #self.pca.servo[fingure].angle = j
          self.servoValues[fingure] =j #self.pca.servo[fingure].angle
          time.sleep(0.001)

      #self.pca.servo[fingure].angle=None #disable channel
      time.sleep(0.5)





  def ReleaseAll(self):

      for servo in self.Servo_list:

          servo.setAngle(None) #disable channel
