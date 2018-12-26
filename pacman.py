import turtle
import os
import math
import random

# create a blank screen that serves as background
game=turtle.Screen()
game.bgcolor("black")
game.title("Pacman")
randomnumone=random.randint(0,1)

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
    # enemy one converges onto pacman's x location
    if (randomnumone==0 or enemyone.ycor()==protagonist.ycor()):
        enemyonehorizontallocation=enemyone.xcor()
        if (enemyonehorizontallocation<protagonist.xcor()):
            enemyonehorizontallocation+=1
            enemyone.setx(enemyonehorizontallocation)
        elif (enemyonehorizontallocation>protagonist.xcor()):
            enemyonehorizontallocation-=1
            enemyone.setx(enemyonehorizontallocation)
        else:
            enemyone.setx(protagonist.xcor())
    # enemy one converges onto pacman's y location
    if (randomnumone==1 or enemyone.xcor()==protagonist.xcor()):
        enemyoneverticallocation=enemyone.ycor()
        if (enemyoneverticallocation<protagonist.ycor()):
            enemyoneverticallocation+=1
            enemyone.sety(enemyoneverticallocation)
        elif (enemyoneverticallocation>protagonist.ycor()):
            enemyoneverticallocation-=1
            enemyone.sety(enemyoneverticallocation)
        else:
            enemyone.sety(protagonist.ycor())

    # game over screen :(
    if (enemyone.xcor()==protagonist.xcor() and enemyone.ycor()==protagonist.ycor()):
        gameover=turtle.Turtle()
        gameover.speed(0)
        gameover.color("white")
        gameover.penup()
        gameover.setposition(0,0)
        gameover.write("Game over",False,align="center",font=("Arial",20,"normal"))
