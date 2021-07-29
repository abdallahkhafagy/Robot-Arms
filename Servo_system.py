# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:05:57 2021

@author: Abdullah
"""
from Servo import Servo
import json
import time
from os import path

class Servo_system:
  Driver = None;
  Servo_indeicies = None
  Servo_list = []
  Servo_list_dict = {}
  MIN_IMP=0
  MAX_IMP=0

  MIN_ANG=0
  MAX_ANG=0
  servoValues = []
  path=''


  def __init__(self,driver, index_list,initial_angles,max_angles,min_angles, MIN_IMP,MAX_IMP,file=''):
      self.Driver = driver
      self.path = file
      self.Servo_indeicies = index_list
      self.MIN_IMP=MIN_IMP
      self.MAX_IMP=MAX_IMP
      self.MIN_ANG=min_angles
      self.MAX_ANG=max_angles
      self.Servo_list=[]
      servoValues = [0]*len(index_list)
      for i in enumerate(index_list):
          #print(i,index_list)
          #print('servo num',i[1])


          servo = Servo(self.Driver, index_list[i[0]],initial_angles[i[0]], max_angles[i[0]],min_angles[i[0]],MIN_IMP[0],MAX_IMP[0])
          self.Servo_list.append(servo)
          servo.setAngle(initial_angles[i[0]])
          #self.Servo_list_dict[i[1]] = servo
          #print(i,len(self.Servo_list))
          #servo.set_pwm_rng();


  def get_servo_count(self):
      return len(self.Servo_list)


#(Note) comment inside this function should be removed for production purposes
  def setAngle(self,finger_ind,angle):
      #for i in range(1,101,1):
      #print("curr angle ",self.Servo_list[finger_ind].current_angle)
      rng = self.get_range(self.Servo_list[finger_ind].current_angle,angle)
      print(rng)
      for j in rng:

          self.Servo_list[finger_ind].setAngle(j)
          #time.sleep(0.01)
          
  def readAction(self,Action):
      #print(Action)
      #print(self.path+'/Actions.json')
      f = open(self.path+'/Actions.json')
      data = json.load(f)
      #print(data)
      if Action in data:
          
          return data[Action]
      else:
          return None

  def runAction(self,action):
      #print(action)
      if path.exists(self.path+'/Actions.json'):
          Action = self.readAction(action)
          print(Action)
          if Action is not None:
              
          
          

              
              #print(Action)
              
              while True:
                  #print("loop")
                  bool_arr = []
                  
                  
               
                  for servo in self.Servo_list:
                      #print("servo num",str(servo.motor_num))
                      #print("angle ",Action['angles'][str(servo.motor_num)])
                      
                      #print("current",servo.current_angle)
                      if str(servo.motor_num) in Action['angles']:
                          
                          rng = self.get_range(servo.current_angle,Action['angles'][str(servo.motor_num)],1)
                      
                          #print(len(rng))
                           
                          if len(rng) > 1:
                            
                              servo.setAngle(servo.current_angle)
                              servo.setAngle(rng[1])
                              
                              bool_arr.append(servo.current_angle == rng[len(rng)-1])
                              
                            
                          else:
                              z=1
                              #print("range",rng[0])
                              #print("CURRENT",servo.motor_num)
                              #print("CURRENT",servo.current_angle)
                              #print(bool_arr)
                              #continue
                              #servo.setAngle(rng[0])
                              #bool_arr.append(servo.current_angle == rng[len(rng)-1])
                      time.sleep(0.01)
                      #print("bool arr",(False not in bool_arr))
                  if (False not in bool_arr):
                      
                      print("break")
                      break










  def get_range(self,curr_angle,dist_angle,step=1):
      #print(dist_angle,curr_angle)
      if curr_angle<= dist_angle:
          return range(curr_angle,dist_angle,step)
      else:
          #print("hi")
          return range(dist_angle,curr_angle,step)
