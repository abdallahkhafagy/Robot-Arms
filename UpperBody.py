import os
#print(os.walk("/Hand"))
import json
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from Hand import Hand
from Shoulder import Shoulder

import time    #https://docs.python.org/fr/3/library/time.html


class UpperBody():
    dir_path = None
    MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
    MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]


    def __init__(self):
        

        self.dir_path = os.path.dirname(os.path.realpath(__file__))




        f = open(self.dir_path+'/config.json',)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Iterating through the json
        # list
        #for i in data['emp_details']:
        self.RHandDriver = None
        self.RHand = None
        self.RShoulder = None
        self.list = []
        #print(data['Body_parts'])
        for part in data['Body_parts']:
            print(data['Body_parts'])
            if part['name'] == "Right Hand":
                addr = (int(part['address'],16))
                #print(addr)
                self.RHandDriver = ServoKit(channels=16,address = addr)
                for piece in part['parts']:
                    self.list.append(piece['file'])
                    path = self.dir_path+piece['file']
                    if piece['name'] == 'Hand':
                        self.RHand = Hand(self.RHandDriver,piece['indicies'],piece['initialAngles'],piece['MaxAngles'],piece['MinAngles'],self.MIN_IMP,self.MAX_IMP,path)
                    elif piece['name'] == 'Shoulder':
                        self.RShoulder = Shoulder(self.RHandDriver,piece['indicies'],piece['initialAngles'],piece['MaxAngles'],piece['MinAngles'],self.MIN_IMP,self.MAX_IMP,path)








        # Closing file
        f.close()


    def runScenario(self,scenario_name):
        
        #for file in os.listdir(dir_path+"/Scenarios/Scenarios.json"):

        f = open(self.dir_path+'/Scenarios/Scenarios.json',)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        scenario_data = None
        if scenario_name in data:
            scenario_data = data[scenario_name]
        index = 0
        for action in scenario_data['Actions']:
            time.sleep(scenario_data['Delay'][index])
            print(action)
            print("Delay",scenario_data['Delay'])
            self.RHand.runAction(action)
            self.RShoulder.runAction(action)



            index+=1
