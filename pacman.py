import turtle
import time
import os
import math
import random
from redenemy import Redenemy
from pinkenemy import Pinkenemy
from orangeenemy import Orangeenemy
from blueenemy import Blueenemy


# create a blank screen that serves as background
game=turtle.Screen()
game.bgcolor("black")
game.title("Pacman")
randomnumone=random.randint(0,1)
randomnumtwo=random.randint(0,1)
randomnumthree=random.randint(0,1)
randomnumfour=random.randint(0,1)


movementspeed=20
border=280

boundary=turtle.Turtle()
boundary.speed(0)
boundary.color("white")
boundary.penup()
boundary.setposition(-300,-300)
boundary.pendown()
boundary.pensize(3)
for eachline in range(4):
    boundary.fd(600)
    boundary.lt(90)
# hides the triangle used to draw boundaries
boundary.hideturtle()

# creating walls
wall=turtle.Turtle()
wall.speed(0)
wall.color("white")
wall.penup()
wall.setposition(-270,-270)
wall.pendown()
wall.pensize(3)
pointerx= -270
pointery= -270

#create a square wall
while(pointery<280):
    while (pointerx < 280):
        for eachline in range(4):
            wall.fd(60)
            wall.lt(90)
        wall.penup()
        pointerx=pointerx+100
        wall.setposition(pointerx,pointery)
        wall.pendown()
    wall.penup()
    pointery=pointery+100
    pointerx=-370
    wall.setposition(pointerx,pointery)






#creating pacman
protagonist=turtle.Turtle()
protagonist.color("yellow")
protagonist.shape("circle")
protagonist.penup()
protagonist.speed(0)
protagonist.setposition(0,-150)

#creating first enemy
enemyone=turtle.Turtle()
enemyone.color("red")
enemyone.shape("triangle")
enemyone.penup()
enemyone.speed(0)
enemyone.setposition(-150,150)
enemyone.setheading(270)

#create second enemy
enemytwo=turtle.Turtle()
enemytwo.color("pink")
enemytwo.shape("triangle")
enemytwo.penup()
enemytwo.speed(0)
enemytwo.setposition(-50,150)
enemytwo.setheading(270)

# create third enemy
enemythree=turtle.Turtle()
enemythree.color("light blue")
enemythree.shape("triangle")
enemythree.penup()
enemythree.speed(0)
enemythree.setposition(50,150)
enemythree.setheading(270)

# create fourth enemy
enemyfour=turtle.Turtle()
enemyfour.color("orange")
enemyfour.shape("triangle")
enemyfour.penup()
enemyfour.speed(0)
enemyfour.setposition(150,150)
enemyfour.setheading(270)


#adds methods that allows player to move
def lef():
    x=protagonist.xcor()
    x -= movementspeed
    if x<=-border:
        x=-border
    protagonist.setx(x)

def rig():
    x=protagonist.xcor()
    x += movementspeed
    if x>=border:
        x=border
    protagonist.setx(x)

def up():
    y=protagonist.ycor()
    y += movementspeed
    if y>=border:
        y=border
    protagonist.sety(y)

def down():
    y=protagonist.ycor()
    y -= movementspeed
    if y<=-border:
        y=-border
    protagonist.sety(y)

#creating keyboard functions
turtle.listen()
turtle.onkey(lef,"Left")
turtle.onkey(rig,"Right")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")

while True:
    one = Redenemy(protagonist.xcor(), protagonist.ycor(), enemyone.xcor(), enemyone.ycor())
    two = Pinkenemy(protagonist.xcor(),protagonist.ycor(),enemytwo.xcor(),enemytwo.ycor())
    three = Orangeenemy(protagonist.xcor(),protagonist.ycor(),enemythree.xcor(),enemythree.ycor())
    four = Blueenemy(protagonist.xcor(),protagonist.ycor(),enemyfour.xcor(),enemyfour.ycor())

    if (randomnumone==0 or protagonist.ycor()==enemyone.ycor()):
        enemyone.setx(one.xmovement())
    if (randomnumone==1 or protagonist.xcor()==enemyone.xcor()):
        enemyone.sety(one.ymovement())

    if (randomnumtwo==0 or protagonist.ycor()==enemytwo.ycor()):
        enemytwo.setx(two.xmovement())
    if (randomnumtwo==1 or protagonist.xcor()==enemytwo.xcor()):
        enemytwo.sety(two.ymovement())

    if (randomnumthree==0 or protagonist.ycor()==enemythree.ycor()):
        enemythree.setx(three.xmovement())
    if (randomnumthree==1 or protagonist.xcor()==enemythree.xcor()):
        enemythree.sety(three.ymovement())

    if (randomnumfour==0 or protagonist.ycor()==enemyfour.ycor()):
        enemyfour.setx(four.xmovement())
    if (randomnumfour==1 or protagonist.xcor()==enemyfour.xcor()):
        enemyfour.sety(four.ymovement())



    # game over screen :(
    if (one.gameover()==True or two.gameover()==True or three.gameover()==True or four.gameover()==True):
        gameover=turtle.Turtle()
        gameover.speed(0)
        gameover.color("white")
        gameover.penup()
        gameover.setposition(0,0)
        gameover.write("Game over",False,align="center",font=("Arial",20,"normal"))
        turtle.onkey(None, "Left")
        turtle.onkey(None, "Right")
        turtle.onkey(None, "Up")
        turtle.onkey(None, "Down")
        time.sleep(5)
        exit()

