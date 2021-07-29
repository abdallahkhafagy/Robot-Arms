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








  def ReleaseAll(self):

      for servo in self.Servo_list:

          servo.setAngle(None) #disable channel
