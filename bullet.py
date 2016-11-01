from turtle import *
import math

s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

class Bullet(RawTurtle):
    def __init__(self, canvas, x, y, direc, dx, dy):
        super().__init__(canvas)
        self.penup()
        self.goto(x, y)
        self.setheading(direc)
        self.color("Red")
        self.lifespan = 200
        self.dx = math.cos(math.radians(direc)) * 2 + dx
        self.dy = math.sin(math.radians(direc)) * 2 + dy
        self.shape("bullet")

    def getLifeSpan(self):
        return self.lifespan

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def getRadius(self):
        return 4

    def update(self):
        self.lifespan -= 1
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        up_x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        up_y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(up_x, up_y)
