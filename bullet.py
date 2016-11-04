from turtle import *
import math

#screen sizes
s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

class Bullet(RawTurtle):
    #init all values for the bullet
    def __init__(self, canvas, x, y, direc, dx, dy, color):
        super().__init__(canvas)
        self.penup()
        self.goto(x, y)
        self.color(color)
        self.setheading(direc)
        self.lifespan = 100
        self.dx = math.cos(math.radians(direc)) * 10 + dx
        self.dy = math.sin(math.radians(direc)) * 10 + dy
        dist = math.sqrt(self.dx**2 + self.dy**2)
        self.shape("circle")
        self.shapesize(.25, .25, .25)

    #update position on the screen
    def update(self):
        #decrease how many uppdates to can go through
        self.lifespan -= 1
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        #make sure new position is on the screen
        up_x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        up_y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(up_x, up_y)
    
    #getters
    def getLifeSpan(self):
        return self.lifespan

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def getRadius(self):
        return .25
