from turtle import Turtle, Screen, colormode
from random import randint

tm = Turtle()
colormode(255)
tm.speed(0)
gap_size = 5
for _ in range(int(360/gap_size)):
    tm.color((randint(0,255),randint(0,255),randint(0,255)))
    tm.circle(100)
    tm.left(gap_size)

sc = Screen()
sc.exitonclick()