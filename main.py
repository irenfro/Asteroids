from turtle import *
import tkinter.messagebox
import tkinter
import random
import asteroid
import player

s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

def main():
    root = tkinter.Tk()
    root.title("Asteroids")
    cv = ScrolledCanvas(root, s_size + 100, s_size + 100, s_size + 100, s_size + 100)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)

    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX, screenMinY, screenMaxX, screenMaxY)
    screen.register_shape("ast3",((-20, -16),(-21, 0), (-20,18),(0,27),(17,15),(25,0),(16,-15),(0,-21)))
    screen.register_shape("ast2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
    screen.register_shape("ast1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
    screen.register_shape("ship", ((-10, -10), (0, -5), (10, -10), (0, 10)))
    screen.register_shape("bullet", ((-2, -4), (-2, 4), (2, 4), (2, -4)))
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
    t.ht()
    
    def quitHandler():
        root.destroy()
        root.quit()

    quitButton = tkinter.Button(frame, text = "Quit", command = quitHandler)
    quitButton.pack()

    screen.tracer(10)

    ship = player.Player(cv,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY)

    asteroids = []

    for a in range(10):
        dx = random.random() * 6 - 3
        dy = random.random() * 6 - 3
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        ast = asteroid.Asteroid(cv, dx, dy, x, y, 3)
        asteroids.append(ast)
    
    def turnLeft():
        ship.setheading(ship.heading() + 7)
    
    def turnRight():
        ship.setheading(ship.heading() - 7)
    
    def forward():
        ship.move()
    
    def play():
        ship.update()
        for asteroid in asteroids:
            asteroid.update()
        screen.ontimer(play, 5)

    screen.ontimer(play, 5)

    screen.onkeypress(turnLeft, "Left")
    screen.onkeypress(turnRight, "Right")
    screen.onkeypress(forward, "Up")
    
    screen.listen()
    
    tkinter.mainloop()



if __name__ == "__main__":
    main()
