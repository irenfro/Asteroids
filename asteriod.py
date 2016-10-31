from turtle import *

s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

class Asteroid(RawTurtle):
    def __init__(self, canvas, dx, dy, x, y, size):
        RawTurtle.__init__(self, canvas)
        self.penup()
        self.goto(x, y)
        self.size = size
        self.dx = dx
        self.dy = dy
        self.shape("ast" + str(size))

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

    def update(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        up_x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        up_y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY

        self.goto(up_x, up_y)

    def getRad(self):
        return self.size * 10 - 5
