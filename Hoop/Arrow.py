#Author: Ishan Mani Subedi

# importing the visual library
from visual import *

# setting up the scene
myscene = display(title ="Arrow")
myscene.autoscale = False
class Arrow(object):

    # Constructor
    def __init__(self, xPos, yPos, zPos, xaxis, yaxis, zaxis, width):
        self._xPos = xPos
        self._yPos = yPos
        self._zPos = zPos
        self._xaxis = xaxis
        self._yaxis = yaxis
        self._zaxis = zaxis
        self._width = width
        
    
    #uses Vpython to draw an arrow.
    def drawArrow(self):
        pointer = arrow(pos=(self._xPos,self._yPos,self._zPos),axis=(self._xaxis,self._yaxis,self._zaxis), shaftwidth=self._width,material=materials.wood)
        return pointer
    
    #setters and getters
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

