import turtle
import os
import math
import random

# create a blank screen that serves as background
game=turtle.Screen()
game.bgcolor("black")
game.title("Pacman")

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


turtle.mainloop()