# Author: Ishan Subedi

from Arrow import *
from Ball import  *
from Hoop import *


myscene = display(title ="Ishan's Game",background = (0,0,0))
myscene.fullscreen = True
myscene.autoscale = False
myscene.width = 800
myscene.height = 800
text_game = '''The aim of this game is get the ball inside the Hoop. You have 50 chances to get 10 balls

inside the Hoop before the game stops. The only control is the physical object by the sensor
              
it only moves from left to right. Lifting the physical object will pause the game.For best

performace perform the upload on the Arduino program right before starting the game. Enjoy!!!'''


a = text(text='The game of HOOOOPPPP',pos=(0,2,0),
    align='center', depth=4, color=color.red)

b = label(pos=(0,-1,0), text=text_game,border = 0)
             
c = text(text='Single click to begin',pos=(0,-6,0),
    align='center', depth=-5, color=color.white)          
            


def start():
    while True:
        if myscene.mouse.clicked:
            a.visible = False
            b.visible = False
            c.visible = False
            
            initialize()
        else:
            pass
    
    
def initialize():
    
    a1 = Arrow(-10,6,0,0,-1,0,0.5)
    a2 = Arrow(-8,6,0,0,-1,0,0.5)
    a3 = Arrow(-6,6,0,0,-1,0,0.5)
    a4 = Arrow(-4,6,0,0,-1,0,0.5)
    a5 = Arrow(-2,6,0,0,-1,0,0.5)
    a6 = Arrow(0,6,0,0,-1,0,0.5)
    a7 = Arrow(2,6,0,0,-1,0,0.5)
    a8 = Arrow(4,6,0,0,-1,0,0.5)
    a9 = Arrow(6,6,0,0,-1,0,0.5)
    a10 = Arrow(8,6,0,0,-1,0,0.5)
    a11 = Arrow(10,6,0,0,-1,0,0.5)

    h = Hoop(0,0,0,0,5,2,0.1,1)
    a1.drawArrow()
    a2.drawArrow()
    a3.drawArrow()
    a4.drawArrow()
    a5.drawArrow()
    a6.drawArrow()
    a7.drawArrow()
    a8.drawArrow()
    a9.drawArrow()
    a10.drawArrow()
    a11.drawArrow()

    b1  = ball(0,-5,0,0,0.5,0,0.2)
    h.movehoop()
    


start()





