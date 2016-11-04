from turtle import *
import random

#screen sizes
s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

class Asteroid(RawTurtle):
    #init all values for the asteroid
    def __init__(self, canvas, dx, dy, x, y, size):
        RawTurtle.__init__(self, canvas)
        self.penup()
        self.goto(x, y)
        self.size = size
        self.dx = dx
        self.dy = dy
        self.shape("ast" + str(size))
        #make it rotate in a random direction
        self.rotation = random.random() * 5

    #update position on the screen
    def update(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()
        
        #mkae sure the new position is on the screen
        up_x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        up_y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(up_x, up_y)
        #update the orientation of the asteroid to look like it is spinning
        self.setheading(self.heading() + self.rotation)

    #getters
    def getRadius(self):
        return self.size * 10 - 5
    
    def getSize(self):
        return self.size

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def setDx(self, dx):
        self.dx = dx

    def setDy(self, dy):
        self.dy = dy
