import turtle
import math

# Problem: draw a pyramid

x = turtle.Turtle(shape = 'turtle')

options = ["red", "green", "blue", "brown", "sky blue"]

x.pensize(3)

n = 5
size = 70

x.color(options[0])
x.left(60)
x.forward(size)
x.right(120)
x.forward(size)
x.right(120)
x.forward(size)

height = math.sqrt(size**2 - (size/2)**2)

for i in range(1, 5):
    x.color(options[i])
    x.penup()
    position = x.pos()
    x.setpos(position[0] - size/2, position[1] - height)
    x.left(180)
    x.pendown()
    for j in range(i+1):
        x.left(60)
        x.forward(size)
        x.right(120)
        x.forward(size)
        x.left(60)
    x.right(180)
    x.forward(size*(i+1))

x.left(180)
