import os
#print(os.walk("/Hand"))
import json
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from Hand import Hand
import time    #https://docs.python.org/fr/3/library/time.html



MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

for file in os.listdir(dir_path+"/Actions/Hand"):
    print(file)
    
f = open(dir_path+'/config.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
#for i in data['emp_details']:
RHandDriver = None
RHand = None
#print(data['Body_parts'])
for part in data['Body_parts']:
    print(data['Body_parts'])
    if part['name'] == "Right Hand":
        addr = (int(part['address'],16))
        #print(addr)
        RHandDriver = ServoKit(channels=16,address = addr)
        for piece in part['parts']:
            if piece['name'] == 'Hand':
                RHand = Hand(RHandDriver,piece['indicies'],piece['MaxAngles'],piece['MinAngles'],MIN_IMP,MAX_IMP)

                
    #print(RHandDriver)

    
RHand.openHand()

  
# Closing file
f.close()