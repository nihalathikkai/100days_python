from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.shapesize(0.5)
        self.color('purple')
        self.penup()
        self.refresh()
        
    def rand_pos(self):
        return (20*randint(-14,14),20*randint(-14,14))
        
        
    def refresh(self, positions=[]):
        new_pos = self.rand_pos()
        while new_pos in positions:
            new_pos = self.rand_pos()
        self.goto(new_pos)