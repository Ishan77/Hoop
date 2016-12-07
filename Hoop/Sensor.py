#Author: Ishan Subedi
#This code talks with arduino and gets the data.
import serial

class sensor(object):
    def __init__(self):
        self.arduinoSerialData = serial.Serial("/dev/cu.usbmodem2411",9600) #probably have to change this


    def getLength(self):
        
        
        if (self.arduinoSerialData.inWaiting()>0):
            
            myData = str(self.arduinoSerialData.readline())
            list1 = myData.split(",")
            c = (list1[1])
            return c

ser = sensor()
while True:
    
    d = ser.getLength()
    print(d)
    
            
            


