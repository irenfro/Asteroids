from turtle import *
import math

#max distance in each direction
max_speed = 25

#screen size
s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

class Player(RawTurtle):
    #init all values for player
    def __init__(self,canvas,dx,dy,x,y):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.shape("ship")

    #move the ship on the screen to the new position
    def update(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        #make sure the new positions are on the screen
        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        
        self.goto(x,y)

    #increase of decrease the dx and dy of the player and change the direction the player is facing
    def move(self, direction):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        if(self.dx < max_speed and self.dx > -max_speed):
            self.dx += (x * direction)
        if(self.dy < max_speed and self.dy > -max_speed):
            self.dy += (y * direction)
   
   #getters
    def getRadius(self):
        return 2
    
    def getDx(self):
        return self.dx
    
    def getDy(self):
        return self.dy
