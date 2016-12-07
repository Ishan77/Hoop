#Author : Ishan Subedi

from visual import *

from singleton import *

import serial

from  Ball import *


# Class inherits from a singleton parent.
class Hoop(singleton):

    def __init__(self, xPos, yPos, zPos, xaxis, yaxis, zaxis, width,radius):
            self._xPos = xPos
            self._yPos = yPos
            self._zPos = zPos
            self._xaxis = xaxis
            self._yaxis = yaxis
            self._zaxis = zaxis
            self._width = width
            self._radius = radius
            self.arduinoSerialData = serial.Serial("/dev/cu.usbmodem2641",9600)
            self.ball2 = ball(0,-5,0,0,0.7,0,0.5)
                
        
    
    # Draws the hoop.
    def drawHoop(self):
        hoop = ring(pos=(self._xPos,self._yPos,self._zPos),axis=(self._xaxis,self._yaxis,self._zaxis), radius = self._radius,
                    thickness =self._width)
        return hoop
        
    
    # Getters and setters
    def setx(self,x):
        self._xPos = x
    
    def sety(self,y):
        self._yPos = y
    
    def setz(self,z):
        self._zPos = z
    
    def setxaxis(self,xaxis):
        self._xaxis = xaxis
    
    def setyaxis(self,yaxis):
        self._yaxis = yaxis
    
    def setzaxis(self,zaxis):
        self._zaxis = zaxis

    def getx(self):
        return self._xPos

    def gety(self):
        return self._yPos

    def getz(self):
        return self._zPos

    def getxaxis(self):
        return self._xaxis
    
    def getyaxis(self):
        return self._yaxis
    
    def getzaxis(self):
        return self._zaxis

    def setwidth(self,width):
        self._width = width

    def getwidth(self):
        return self._width

    def setradius(self,radius):
        self._width = width

    def getradius(self):
        return self._radius

    # This code talks with the arduino and moves the Hoop with the user movement.
    def movehoop(self):
        score = 0
        Toop = self.drawHoop()
        ballu = self.ball2.drawball()
        while True:
            
            #if (self.arduinoSerialData.inWaiting()>0):
                 
                 
                 # reading data from arduino
                 myData = str(self.arduinoSerialData.readline())
                 list1 = myData.split(",")
                 try:
                     
                     c = float((list1[1]))
                 except (ValueError,IndexError):
                     
                     c = 0
                 try:  
                     
                     print(c)

                     # Callibiraton
                     if c<20:
                         Toop.pos=(c-9,0,0)
                         
                         self.ball2.yPos = self.ball2.yPos+self.ball2.yvelocity

                         ballu.pos = (self.ball2.getx(),self.ball2.yPos,0)
                         ballu.color= self.ball2.getrung()

                         if self.ball2.detectcollison():
                             ballu.color = self.ball2.getrung()

                         if (abs((self.ball2.getx()-(c-9))))<0.3 and (self.ball2.gety()<1):
                             score = score + 100
                             fext = "Score"+" "+str(score)
                             b = label(pos=(-10,5,0), text=fext,border = 0)
                             
                     else:
                         self.setx(0)

                 except (ValueError,IndexError):
                     Toop.pos(c,0,0)

                 #paddle.visible= False
                
            

  
        
        
        
        







    
