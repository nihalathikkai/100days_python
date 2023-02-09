from turtle import Turtle, Screen

tim = Turtle()

tim.pu()
tim.goto(50,50)
tim.pd()
for _ in range(4):
    tim.right(90)
    tim.forward(100)
    
sc = Screen()
sc.exitonclick()