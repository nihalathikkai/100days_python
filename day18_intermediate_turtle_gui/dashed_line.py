from turtle import Turtle, Screen

tr = Turtle()
for _ in range(15):
    tr.pd()
    tr.forward(10)
    tr.pu()
    tr.forward(10)


sc = Screen()
sc.exitonclick()