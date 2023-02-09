# import colorgram

# colors = colorgram.extract('hirst.jpg', 21)
# colors = [(clr.rgb.r, clr.rgb.g, clr.rgb.b) for clr in colors]
# print(colors)

colors = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 4), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191)]

from turtle import Turtle, Screen, colormode
from random import choice
tm = Turtle()
sc = Screen()
tm.speed(0)
tm.hideturtle()

colormode(255)
tm.pu()
tm.goto((-225,-225))
for i in range(10):
    for j in range(10):
        tm.dot(20,choice(colors))
        tm.forward(50)
    tm.setheading(90)
    tm.forward(50)
    tm.setheading(0)
    tm.backward(500)

sc.exitonclick()