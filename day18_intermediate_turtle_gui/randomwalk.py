from turtle import Turtle, Screen, colormode
from random import randint

tm = Turtle()
tm.pensize(10)
colormode(255)
tm.speed(0)
for _ in range(200):
    tm.color((randint(0,255),randint(0,255),randint(0,255)))
    tm.setheading(90*randint(0,3))
    tm.forward(30)



sc = Screen()
sc.exitonclick()