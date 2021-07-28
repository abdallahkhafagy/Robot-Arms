# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:47:27 2021

@author: Abdullah
"""
#remember to replace limit with max
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
import time

class Servo:
  Driver = None;
  current_angle = 0;
  angle_limit = 0;
  angle_max = 0;
  angle_min = 0;
  motor_num = 0;
  motor_index = 0
  initial_angle = 0
  MIN_IMP = 0 ;
  MAX_IMP = 0;
  f = 1

  def __init__(self, driver, index,initial_angle,max_angle,min_angle,MIN_IMP,MAX_IMP):
      self.motor_num = index
      self.Driver =  driver
      self.angle_max = max_angle
      self.angle_min = min_angle
      self.MIN_IMP =MIN_IMP
      self.MAX_IMP =MAX_IMP
      self.initial_angle = initial_angle
      self.setAngle(initial_angle)


#(Note) comment inside this function should be removed for production purposes
  def setAngle(self,angle):
      if angle is not None:
          if angle in range(self.angle_min,self.angle_max+1) or angle in range(self.angle_max, self.angle_min+1):

              #if angle  != self.current_angle:
              self.Driver.servo[self.motor_num].angle = angle
          self.current_angle = angle

      else:
           self.Driver.servo[self.motor_num].angle = angle


  def getAngle(self):
      return self.current_angle




  def setAngleDelta(self,Delta):

      print("Delta:"+str(Delta),"angle_limit :"+str(self.angle_limit),"current_angle :"+str(self.current_angle))
      if (self.current_angle+Delta) < self.angle_limit:
          if self.current_angle+Delta  != self.current_angle:
              #Driver.servo[self.motor_num] = angle
              print("test set Angle With Angle :"+str(self.current_angle+Delta))
      self.current_angle = self.current_angle+Delta


  def set_pwm_rng(self):
      self.Driver.servo[self.motor_num].set_pulse_width_range(self.MIN_IMP , self.MAX_IMP)
