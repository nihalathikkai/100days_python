from turtle import Turtle, Screen, listen

tm = Turtle()
sc = Screen()

def frwd():
    tm.forward(10)
    
def bkwd():
    tm.backward(10)
    
def left():
    tm.left(10)

def right():
    tm.right(10)
    
def reset():
    tm.clear()
    tm.speed(0)
    tm.pu()
    tm.home()
    tm.setheading(0)
    tm.pd()
    tm.speed(6)

sc.onkeypress(frwd, key='w')
sc.onkeypress(bkwd, key='s')
sc.onkeypress(left, key='a')
sc.onkeypress(right, key="d")
sc.onkeyrelease(reset, key='c')

sc.listen()
sc.exitonclick()