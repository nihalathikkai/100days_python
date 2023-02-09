from turtle import Turtle, Screen
from random import randint

sc = Screen()
sc.setup(width=500,height=400)
sc.colormode(255)
sc.bgcolor(235, 250, 162)


colors = ['red','orange','brown','green', 'blue', 'purple']
lane = [-75,-45,-15,15,45, 75]
start = -230
end = 220
step = 5

def draw_line(x=0, offset=15):
    line = Turtle()
    line.speed(0)
    line.hideturtle()
    line.pu()
    line.goto(x+offset, lane[-1]+50)
    line.pd()
    line.goto(x+offset, lane[0]-50)
    
draw_line(start, 15)
draw_line(end, -10)

turtles = []

for i in range(6):
    tr = Turtle(shape='turtle')
    tr.speed(0)
    tr.color(colors[i])
    tr.penup()
    tr.goto(start, lane[i])
    tr.speed(6)
    turtles.append(tr)
    
    
guess = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color").strip().lower()

while True:
    tr = randint(0,5)
    turtles[tr].forward(step)
    if turtles[tr].position()[0] >= end:
        print(f"Turtle {colors[tr]} finished first!")
        print(f"You have {'won'if colors[tr] == guess else 'lost'} the bet")            
        break


sc.exitonclick()