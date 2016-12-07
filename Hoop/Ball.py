#Author: Ishan Subedi

from visual import *
from Arrow import*
import random
import serial


myscene = display(title ="Ishan's Game")
myscene.autoscale = False


class ball(object):
    list_supple=[(1,1,1)]

    # The constructor to set up the ball dimension.
    def __init__(self,xPos,yPos,zPos,xvelocity,yvelocity,zvelocity ,radius):
        
        
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.radius = radius
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.zvelocity = zvelocity
        #self.arduinoSerialData = serial.Serial("/dev/cu.usbmodem2411",9600)
        #self.paddle = Hoop(0,0,0,0,5,2,0.1,1)
        

    # using Vpython to draw the ball
    def drawball(self):
         

        c = self.getrung()
        ballu = sphere(pos=(self.xPos,self.yPos,self.zPos), radius = self.radius,color =c)
        self.autoscale = False
        return ballu
       
       
   # Setters and getters.
    def setx(self,x):

        self.xPos = x

    def sety(self,y):

        self.yPos = y

    def setz(self,z):

        self.zPos = z

    def getx(self):

        return self.xPos

    def gety(self):

        return self.yPos

    def getz(self):
        
        return zPos
    

    def getrung(self):
        
        listcolor=[]
       
        tuple_red = (1,0,0)
        tuple_green = (0,1,0)
        tuple_blue = (0,0,0.5)
        
        listcolor.append(tuple_red)
        listcolor.append(tuple_green)
        listcolor.append(tuple_blue)

        random_color = random.randint(0,2)

        

        if self.yPos > 4:
           
            ball.list_supple[0]=listcolor[random_color]

            return listcolor[random_color]

        else: 
            return ball.list_supple[0]
        
            
    def moveball(self):
        
        t = 0
        while t < 3:
            rate(10000)
            ballu = self.drawball()
            rate(5)
            self.sety(self.yPos+self.yvelocity)
            ballu.visible= False
            self.detectcollison()

    def detectcollison(self):
       
       
       if self.yPos > 5: 
           self.yPos=-6
           self.xPos = random.randint(-10,10)
           return True
        
 



        
        
