# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:55:55 2021

@author: Abdullah
"""
from Servo_system import Servo_system

class Wrist(Servo_system):

  def __init__(self, index, driver,max_angle,min_angle):
      super().__init__( index, driver,max_angle,min_angle)
     
      
      
#(Note) comment inside this function should be removed for production purposes
  def setAngle(self,angle):
      
      print("angle:"+str(angle),"angle_limit :"+str(self.angle_limit),"current_angle :"+str(self.current_angle))
      if angle < self.angle_limit:
          if angle  != self.current_angle:
              #Driver[self.motor_num] = angle
              print("test set Angle With Angle :"+str(angle))
      self.current_angle = angle
              
      
  def setAngleDelta(self,Delta):
      
      print("Delta:"+str(Delta),"angle_limit :"+str(self.angle_limit),"current_angle :"+str(self.current_angle))
      if (self.current_angle+Delta) < self.angle_limit:
          if self.current_angle+Delta  != self.current_angle:
              #Driver[self.motor_num] = angle
              print("test set Angle With Angle :"+str(self.current_angle+Delta))
      self.current_angle = self.current_angle+Delta
              
      
    