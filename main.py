from turtle import *
import tkinter.messagebox
import tkinter.colorchooser
import datetime
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
#ship color
sh_color = "Cyan"
#bullet color
bul_color = "Red"
#root view
root = tkinter.Tk()
#if the user changed the color
c_change = False

#method for choosing a custom hex value for ship
def custHex():
    global sh_color
    global c_change
    temp = tkinter.colorchooser.askcolor(sh_color, title="Choose Ship Color", parent=root)
    if not (temp[1] == None):
        sh_color = temp[1]
        c_change = True

#method for choosing a custom hex value for bullet
def custHexB():
    global bul_color
    temp = tkinter.colorchooser.askcolor(bul_color, title="Choose Bullet Color", parent=root)
    if not (temp[1] == None):
        bul_color = temp[1]
#Menu methods for ship
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

#Menu methods for Bullet
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

#check is two objects have collided
def intersect(object1,object2):
    dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
    radius1 = object1.getRadius()
    radius2 = object2.getRadius()      
    return dist <= radius1+radius2

#main program
def main():
    global root
    #focus on the main view
    root.lift()
    #init menu
    menubar = tkinter.Menu(root)
    #options menu
    opmenu = tkinter.Menu(menubar, tearoff=0)
    #ship menu under options
    shipmenu = tkinter.Menu(opmenu, tearoff=0)
    #bullet menu uder options
    bulmenu = tkinter.Menu(opmenu, tearoff=0)

    #add commands for the ship colors.  Some base ones like Cyan, Green, Red, Blue, and Yellow
    #also have the option to pick your own color
    shipmenu.add_command(label="Cyan", command=Cyan)
    shipmenu.add_command(label="Green", command=Green)
    shipmenu.add_command(label="Red", command=Red)
    shipmenu.add_command(label="Blue", command=Blue)
    shipmenu.add_command(label="Yellow", command=Yellow)
    shipmenu.add_command(label="Custom Hex Color", command=custHex)


    #add commands for the bullet colors.  Some base ones like Cyan, Green, Red, Blue, and Yellow
    #also have the option to pick your own color
    bulmenu.add_command(label="Cyan", command=CyanB)
    bulmenu.add_command(label="Green", command=GreenB)
    bulmenu.add_command(label="Red", command=RedB)
    bulmenu.add_command(label="Blue", command=BlueB)
    bulmenu.add_command(label="Yellow", command=YellowB)
    bulmenu.add_command(label="Custom Hex Color", command=custHexB)

    #add drop down menus to options
    opmenu.add_cascade(label="Change Ship Color", menu=shipmenu)
    opmenu.add_cascade(label="Change Bullet Color", menu=bulmenu)
    #add the options menu as a drop down menu to the menubar
    menubar.add_cascade(label="Options", menu=opmenu)

    #make the menu visible 
    root.config(menu=menubar)

    #set the title for the window
    root.title("Asteroids")
    #init the canvas for the entire game
    cv = ScrolledCanvas(root, s_size + 100, s_size + 100, s_size + 100, s_size + 100)
    #make the canvas visible
    cv.pack(side = tkinter.LEFT)
    #init a Raw Turtle for drawing everything
    t = RawTurtle(cv)

    #grab the screen
    screen = t.getscreen()
    #set the background image or do screen.bgcolor("black") to set the background to a color
    screen.bgpic("bg.gif")
    #set the screen bounds for the game
    screen.setworldcoordinates(screenMinX, screenMinY, screenMaxX, screenMaxY)
    #register shapes for drawing
    screen.register_shape("ast2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
    screen.register_shape("ast1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
    screen.register_shape("ship", ((-10, -10), (0, -5), (10, -10), (0, 10)))
    screen.register_shape("bullet", ((-2, -4), (-2, 4), (2, 4), (2, -4)))
    #example for making a more complex shape
    s = Shape("compound")
    poly1 = ((-20, -16),(-21, 0),(-20,18),(0,27),(17,15), (25,0),(16,-15),(0,-21))
    s.addcomponent(poly1,"gray","gray")
    poly2 = (( -17, -14),(-12, -12),(-8, -13),(-8, -7),(-12, -8))
    s.addcomponent(poly2, "dark gray", "dark gray")
    poly3 = ((3,2),(6,3),(9,6),(10,9),(6,12),(0,8),(-1,6))
    s.addcomponent(poly3,"dark gray","dark gray")
    screen.register_shape("ast3",s)
    
    #new frame for showing the score, lives and quit button in
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
    
    #init score value
    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    
    #make a score Title
    scoreTitle = tkinter.Label(frame, text = "Score")
    scoreTitle.pack()
    
    #a place the show the score
    scoreFrame = tkinter.Frame(frame, height = 2, bd = 1, relief = tkinter.SUNKEN)
    scoreFrame.pack()
    
    #making a label for score
    score = tkinter.Label(scoreFrame, height = 2, width = 20, textvariable = scoreVal, fg = "Yellow", bg = "black")
    #making it visible
    score.pack()
    
    #title for the remaining lives section
    livesTitle = tkinter.Label(frame, text = "Remaining Lives")
    livesTitle.pack()
    
    #init a place to show the lives
    livesFrame = tkinter.Frame(frame, height = 30, width = 60, relief = tkinter.SUNKEN)
    livesFrame.pack()

    #place to draw the lives
    livesCanvas = ScrolledCanvas(livesFrame, 150, 40, 150, 40)
    livesCanvas.pack()

    #a turtle for drawing the lives
    livesTurtle = RawTurtle(livesCanvas)
    livesTurtle.ht()

    #register a shape in the screen
    livesScreen = livesTurtle.getscreen()
    livesScreen.register_shape("ship", ((-10,-10),(0,-5),(10,-10),(0,10)))

    #draw the lives
    life1 = player.Player(livesCanvas, 0, 0, -35, 0)
    life1.color(sh_color)
    life2 = player.Player(livesCanvas, 0, 0, 0, 0)
    life2.color(sh_color)
    life3 = player.Player(livesCanvas, 0, 0, 35, 0)
    life3.color(sh_color)
    
    lives = [life1, life2, life3]

    t.ht()

    #called when using the quit button
    def quitHandler():
        root.destroy()
        root.quit()

    #make the quit button
    quitButton = tkinter.Button(frame, text = "Quit", command = quitHandler)
    quitButton.pack()

    #we want to update the screen manually
    screen.tracer(0)

    #init the player
    ship = player.Player(cv, 0, 0, (screenMaxX-screenMinX)/2+screenMinX, (screenMaxY-screenMinY)/2 + screenMinY)
    ship.color(sh_color)
    
    #init the array to contain the asteroids and bullets
    asteroids = []
    bullets = []

    #random number of asteroids for the game
    ran = (int)(10 + random.random() * 10)
    for a in range(ran):
        dx = random.random() * 6 - 3
        dy = random.random() * 6 - 3
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        ast = AST.Asteroid(cv, dx, dy, x, y, 3)
        asteroids.append(ast)
    
    #player movement functions for keyevents
    def turnLeft():
        ship.setheading(ship.heading() + 7)
    
    def turnRight():
        ship.setheading(ship.heading() - 7)
    
    def forward():
        ship.move(1)

    def backward():
        ship.move(-1)

    #firing a bullet
    def fire():
        #only have a max of 20 bullets at once to make sure the game doesnt slow down
        if len(bullets) < 20:
            b = bullet.Bullet(cv, ship.xcor(), ship.ycor(), ship.heading(), ship.getDx(), ship.getDy(), bul_color)
            bullets.append(b)
    
    #main place for updating everything
    def play():
        #update the screen
        screen.update()
        #start timer for how lone it takes
        start = datetime.datetime.now()
        global c_change
        #see if a color change happened
        #if yes then update the colors
        if c_change:
            c_change = False
            ship.color(sh_color)
            for l in lives:
                l.color(sh_color)
        #the win case
        if len(asteroids) == 0:
            tkinter.messagebox.showwarning("You Win!", "You Destroyed all the Asteroids!")
            return
        #update where the ship is
        ship.update()
        #make sure the player can only be hit once per screen update
        hit = False
        #update all of the asteroids
        for asteroid in asteroids:
            asteroid.update()
            #check if the player hit an asteroid
            if intersect(asteroid, ship):
                #if there are still lives left
                if len(lives) > 0:
                    #if we were not preivously hit
                    if not hit:
                        tkinter.messagebox.showwarning("You Crashed!", "You Lost a Life")
                        #remove a life
                        s = lives.pop()
                        #hide the ship
                        s.ht()
                        hit = True
                        #remove the asteroid
                        try:
                            asteroids.remove(asteroid)
                        except:
                            print("error removing asteroid")
                        #hide the asteroid
                        asteroid.ht()
                #Game over clause
                else:
                    tkinter.messagebox.showwarning("Game Over", "You lost the game!\nPlease try again")
                    return
        #update all of the bullets
        for bullet in bullets:
            bullet.update()
            #make bullets not last forever
            if bullet.getLifeSpan() <= 0:
                try:
                    bullets.remove(bullet)
                except:
                    print("error removing bullet")
                bullet.ht()
            #see if the bullet hit an asteroid
            else:
                end_ast = []
                for ast in asteroids:
                    #if a bullet hit an asteroid remove the bullet and append the asteroid to a list
                    if intersect(bullet, ast):
                        end_ast.append(ast)
                        try:
                            bullets.remove(bullet)
                        except:
                            print("error removing bullet")
                        bullet.ht()
                        #give the asteroid some movement from the bullet
                        ast.setDx(bullet.getDx() + ast.getDx())
                        ast.setDy(bullet.getDy() + ast.getDy())
                #remove asteroids and increse the points
                for ast in end_ast:
                    try:
                        asteroids.remove(ast)
                    except:
                        print("error removing asteroid")

                    #hide the asteroid
                    ast.ht()
                    size = ast.getSize()

                    score = int(scoreVal.get())

                    #increment score based on size of asteroid
                    if size == 3:
                        score += 20
                    elif size == 2:
                        score += 50
                    elif size == 1:
                        score += 100
                    
                    #display new score
                    scoreVal.set(str(score))

                    #add new asteroids to the array if the asteroids were not the smallest ones
                    if ast.getSize() > 1:
                        dist = math.sqrt(ast.getDx() ** 2 + ast.getDy() ** 2)

                        ast1 = AST.Asteroid(cv, -ast.getDx() / dist, ast.getDy() / dist, ast.xcor(), ast.ycor(), ast.getSize() - 1)
                        ast2 = AST.Asteroid(cv, ast.getDx() / dist, -ast.getDy() / dist, ast.xcor(), ast.ycor(), ast.getSize() - 1)
                        ast1.color("gray")
                        ast2.color("gray")
                        asteroids.append(ast1)
                        asteroids.append(ast2)
        #end the timer
        end = datetime.datetime.now()
        length = end - start
        millis = length.microseconds / 1000.0
        #call the play method again in 10 miliseconds from when it was called
        screen.ontimer(play, int(10 - millis))

    #call the play function for the first time in 5 miliseconds
    screen.ontimer(play, 5)

    #init the key listeners
    screen.onkeypress(turnLeft, "Left")
    screen.onkeypress(turnRight, "Right")
    screen.onkeypress(forward, "Up")
    screen.onkeypress(backward, "Down")
    screen.onkeypress(fire, " ")

    #start listening for the keys
    screen.listen()
    #start the mainloop
    tkinter.mainloop()



if __name__ == "__main__":
    main()
