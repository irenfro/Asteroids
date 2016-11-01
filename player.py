from turtle import *
import math

max_speed = 25

s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

class Player(RawTurtle):
    def __init__(self,canvas,dx,dy,x,y):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.color("cyan")
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.shape("ship")

    def update(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        
        self.goto(x,y)

    def move(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        if(self.dx < max_speed):
            self.dx += x
        if(self.dy < max_speed):
            self.dy += y
   
    def getRadius(self):
        return 2
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy
