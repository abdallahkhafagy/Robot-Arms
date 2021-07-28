# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:56:02 2021

@author: Abdullah
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:54:39 2021

@author: Abdullah
"""
from Servo_system import Servo_system
import time
class Shoulder(Servo_system):

  def __init__(self,driver, index_list, initial_angles,max_angle,min_angle,MIN_IMP,MAX_IMP,path):
      super().__init__( driver,index_list,initial_angles, max_angle,min_angle,MIN_IMP,MAX_IMP,path)







  def setAngleDelta(self,Delta):
      for i in len(self.Servo_list):
          self.Servo_list[self.Servo_list].setAngle(angle)

      print("Delta:"+str(Delta),"angle_limit :"+str(self.angle_limit),"current_angle :"+str(self.current_angle))
      if (self.current_angle+Delta) < self.angle_limit:
          if self.current_angle+Delta  != self.current_angle:
              #Driver[self.motor_num] = angle
              print("test set Angle With Angle :"+str(self.current_angle+Delta))
      self.current_angle = self.current_angle+Delta



  def ReleaseAll(self):

      for servo in self.Servo_list:

          servo.setAngle(None) #disable channel
