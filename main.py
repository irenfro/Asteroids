from turtle import *
import tkinter.messagebox
import tkinter.colorchooser
import random
import math
import asteroid as AST
import player
import bullet

s_size = 500
screenMinX = -s_size
screenMinY = -s_size
screenMaxX = s_size
screenMaxY = s_size

sh_color = "Cyan"
bul_color = "Red"

root = tkinter.Tk()

c_change = False

def hello():
    print("hello")

def custHex():
    global sh_color
    global c_change
    temp = tkinter.colorchooser.askcolor(sh_color, title="Choose Ship Color", parent=root)
    if not (temp[1] == None):
        sh_color = temp[1]
        c_change = True

def custHexB():
    global bul_color
    temp = tkinter.colorchooser.askcolor(bul_color, title="Choose Bullet Color", parent=root)
    if not (temp[1] == None):
        bul_color = temp[1]

def Cyan():
    global sh_color
    sh_color = "Cyan"
    global c_change
    c_change = True
def Green():
    global sh_color
    sh_color = "Green"
    global c_change
    c_change = True
def Red():
    global sh_color
    sh_color = "Red"
    global c_change
    c_change = True
def Blue():
    global sh_color
    sh_color = "Blue"
    global c_change
    c_change = True
def Yellow():
    global sh_color
    sh_color = "Yellow"
    global c_change
    c_change = True

def CyanB():
    global bul_color
    bul_color = "Cyan"
def GreenB():
    global bul_color
    bul_color = "Green"
def RedB():
    global bul_color
    bul_color = "Red"
def BlueB():
    global bul_color
    bul_color = "Blue"
def YellowB():
    global bul_color
    bul_color = "Yellow"

def intersect(object1,object2):
    dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
    radius1 = object1.getRadius()
    radius2 = object2.getRadius()      
    return dist <= radius1+radius2

def main():
    global root
    root.lift()
    menubar = tkinter.Menu(root)
    
    opmenu = tkinter.Menu(menubar, tearoff=0)
    shipmenu = tkinter.Menu(opmenu, tearoff=0)
    bulmenu = tkinter.Menu(opmenu, tearoff=0)

    shipmenu.add_command(label="Cyan", command=Cyan)
    shipmenu.add_command(label="Green", command=Green)
    shipmenu.add_command(label="Red", command=Red)
    shipmenu.add_command(label="Blue", command=Blue)
    shipmenu.add_command(label="Yellow", command=Yellow)
    shipmenu.add_command(label="Custom Hex Color", command=custHex)


    bulmenu.add_command(label="Cyan", command=CyanB)
    bulmenu.add_command(label="Green", command=GreenB)
    bulmenu.add_command(label="Red", command=RedB)
    bulmenu.add_command(label="Blue", command=BlueB)
    bulmenu.add_command(label="Yellow", command=YellowB)
    bulmenu.add_command(label="Custom Hex Color", command=custHexB)

    opmenu.add_cascade(label="Change Ship Color", menu=shipmenu)
    opmenu.add_cascade(label="Change Bullet Color", menu=bulmenu)
    menubar.add_cascade(label="Options", menu=opmenu)

    root.config(menu=menubar)

    root.title("Asteroids")
    cv = ScrolledCanvas(root, s_size + 100, s_size + 100, s_size + 100, s_size + 100)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)

    screen = t.getscreen()
    screen.bgpic("bg.gif")
    screen.setworldcoordinates(screenMinX, screenMinY, screenMaxX, screenMaxY)
    screen.register_shape("ast2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
    screen.register_shape("ast1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
    screen.register_shape("ship", ((-10, -10), (0, -5), (10, -10), (0, 10)))
    screen.register_shape("bullet", ((-2, -4), (-2, 4), (2, 4), (2, -4)))
    
    s = Shape("compound")
    poly1 = ((-20, -16),(-21, 0),(-20,18),(0,27),(17,15), (25,0),(16,-15),(0,-21))
    s.addcomponent(poly1,"gray","gray")
    poly2 = (( -17, -14),(-12, -12),(-8, -13),(-8, -7),(-12, -8))
    s.addcomponent(poly2, "dark gray", "dark gray")
    poly3 = ((3,2),(6,3),(9,6),(10,9),(6,12),(0,8),(-1,6))
    s.addcomponent(poly3,"dark gray","dark gray")
    screen.register_shape("ast3",s)
    
    
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
    
    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    
    scoreTitle = tkinter.Label(frame, text = "Score")
    scoreTitle.pack()
    
    scoreFrame = tkinter.Frame(frame, height = 2, bd = 1, relief = tkinter.SUNKEN)
    scoreFrame.pack()
    
    score = tkinter.Label(scoreFrame, height = 2, width = 20, textvariable = scoreVal, fg = "Yellow", bg = "black")
    score.pack()
    
    livesTitle = tkinter.Label(frame, text = "Remaining Lives")
    livesTitle.pack()
    
    livesFrame = tkinter.Frame(frame, height = 30, width = 60, relief = tkinter.SUNKEN)
    livesFrame.pack()

    livesCanvas = ScrolledCanvas(livesFrame, 150, 40, 150, 40)
    livesCanvas.pack()

    livesTurtle = RawTurtle(livesCanvas)
    livesTurtle.ht()

    livesScreen = livesTurtle.getscreen()
    livesScreen.register_shape("ship", ((-10,-10),(0,-5),(10,-10),(0,10)))

    life1 = player.Player(livesCanvas, 0, 0, -35, 0)
    life1.color(sh_color)
    life2 = player.Player(livesCanvas, 0, 0, 0, 0)
    life2.color(sh_color)
    life3 = player.Player(livesCanvas, 0, 0, 35, 0)
    life3.color(sh_color)
    
    lives = [life1, life2, life3]

    t.ht()

    def quitHandler():
        root.destroy()
        root.quit()

    quitButton = tkinter.Button(frame, text = "Quit", command = quitHandler)
    quitButton.pack()

    screen.tracer(10)

    ship = player.Player(cv,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY)
    ship.color(sh_color)

    asteroids = []
    bullets = []

    ran = (int)(10 + random.random() * 10)
    for a in range(ran):
        dx = random.random() * 6 - 3
        dy = random.random() * 6 - 3
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        ast = AST.Asteroid(cv, dx, dy, x, y, 3)
        asteroids.append(ast)
    
    def turnLeft():
        ship.setheading(ship.heading() + 7)
    
    def turnRight():
        ship.setheading(ship.heading() - 7)
    
    def forward():
        ship.move()

    def fire():
        b = bullet.Bullet(cv, ship.xcor(), ship.ycor(), ship.heading(), ship.getDx(), ship.getDy(), bul_color)
        bullets.append(b)
    
    def play():
        global c_change
        if c_change:
            c_change = False
            ship.color(sh_color)
            for l in lives:
                l.color(sh_color)
        if len(asteroids) == 0:
            tkinter.showmessage.showinfo("You Win!", "You Destroyed all the Asteroids!")
            return
        ship.update()
        for asteroid in asteroids:
            asteroid.update()

            hit = False
            if intersect(asteroid, ship):
                if len(lives) > 0:
                    if not hit:
                        tkinter.messagebox.showwarning("You Crashed!", "You Lost a Life")
                        s = lives.pop()
                        s.ht()
                        hit = True
                        try:
                            asteroids.remove(asteroid)
                        except:
                            print("error removing asteroid")
                        asteroid.ht()
                else:
                    tkinter.messagebox.showwarning("Game Over", "You lost the game!\nPlease try again")
                    return
        for bullet in bullets:
            bullet.update()

            if bullet.getLifeSpan() <= 0:
                try:
                    bullets.remove(bullet)
                except:
                    print("error removing bullet")
                bullet.ht()
            else:
                end_ast = []
                for ast in asteroids:
                    if intersect(bullet, ast):
                        end_ast.append(ast)
                        try:
                            bullets.remove(bullet)
                        except:
                            print("error removing bullet")
                        bullet.ht()
                        ast.setDx(bullet.getDx() + ast.getDx())
                        ast.setDy(bullet.getDy() + ast.getDy())
                for ast in end_ast:
                    try:
                        asteroids.remove(ast)
                    except:
                        print("error removing asteroid")

                    ast.ht()
                    size = ast.getSize()

                    score = int(scoreVal.get())

                    if size == 3:
                        score += 20
                    elif size == 2:
                        score += 50
                    elif size == 1:
                        score += 100

                    scoreVal.set(str(score))

                    if ast.getSize() > 1:
                        dist = math.sqrt(ast.getDx() ** 2 + ast.getDy() ** 2)

                        ast1 = AST.Asteroid(cv, -ast.getDx() / dist, ast.getDy() / dist, ast.xcor(), ast.ycor(), ast.getSize() - 1)
                        ast2 = AST.Asteroid(cv, ast.getDx() / dist, -ast.getDy() / dist, ast.xcor(), ast.ycor(), ast.getSize() - 1)
                        ast1.color("gray")
                        ast2.color("gray")
                        asteroids.append(ast1)
                        asteroids.append(ast2)

        screen.ontimer(play, 5)

    screen.ontimer(play, 5)

    screen.onkeypress(turnLeft, "Left")
    screen.onkeypress(turnRight, "Right")
    screen.onkeypress(forward, "Up")
    screen.onkeypress(fire, " ")

    screen.listen()
    
    tkinter.mainloop()



if __name__ == "__main__":
    main()
