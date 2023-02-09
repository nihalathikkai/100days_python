from turtle import Turtle
from random import choice

MOVE_DISTANCE = 20
START_DIRECTION = (45,135,225,315)

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('white')
        self.setheading(choice(START_DIRECTION))
        self.penup()
        self.move_speed = 0.1
        
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def bounce_y(self):
        # Bounce logic: 45>315;   315>45;     135>225;  225>135
        if self.heading() in (45,225): self.right(90)
        else: self.left(90)
        
    def bounce_x(self):
        # Bounce logic: 45>135;  135>45;    315>225;   225>315
        if self.heading() in (45,225): self.left(90)
        else: self.right(90)
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
        