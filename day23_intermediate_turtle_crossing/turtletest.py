from turtle import Turtle, Screen

BOX = (17,10,-9,-10)

tr = Turtle(shape='turtle')

bx = Turtle()
bx.hideturtle()
bx.penup()

bx.goto(BOX[0], BOX[1])
bx.pendown()
bx.goto(BOX[2], BOX[1])
bx.goto(BOX[2], BOX[3])
bx.goto(BOX[0], BOX[3])
bx.goto(BOX[0], BOX[1])


sc = Screen()
sc.exitonclick()