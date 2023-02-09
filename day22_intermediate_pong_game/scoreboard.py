from turtle import Turtle

FONT = ('Courier', 80, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        
        self.l_score, self.r_score = 0, 0
        self.refresh()
        
        mrkr = Turtle()
        mrkr.color('white')
        mrkr.hideturtle()
        mrkr.penup()
        mrkr.goto(0,-285)
        mrkr.setheading(90)
        mrkr.pensize(5)
        while mrkr.ycor() < 300:
            mrkr.pendown()
            mrkr.forward(20)
            mrkr.penup()
            mrkr.forward(20)
            
    def refresh(self):
        self.clear()
        self.goto(-80, 180)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(+80, 180)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        
    def l_point(self):
        self.l_score += 1
        self.refresh()
        
    def r_point(self):
        self.r_score += 1
        self.refresh()