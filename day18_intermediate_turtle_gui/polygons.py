from turtle import Turtle, Screen, colormode
from random import randint

tm = Turtle()

colormode(255)
tm.pensize(5)
for i in range(3,11):
    tm.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    for _ in range(i):
        tm.right((360/i))
        tm.forward(100)


sc = Screen()
sc.exitonclick()