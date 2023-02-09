from turtle import Turtle

MOVE_DISTANCE = 20
BOUNDARY = 300
OFFSET = 60

class Paddle(Turtle):
    def __init__(self, position: tuple[int,int]):
        super().__init__(shape='square')
        self.color('white')
        self.setheading(90)
        self.shapesize(1,5)
        self.penup()
        self.goto(position)
        
    def up(self):
        if self.ycor() < (BOUNDARY-OFFSET):
            self.forward(MOVE_DISTANCE)
            
    def down(self):
        if self.ycor() > -1* (BOUNDARY-OFFSET):
            self.backward(MOVE_DISTANCE)