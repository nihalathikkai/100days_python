from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        
        self.level = 0
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)
        
    def level_up(self):
        self.level += 1
        self.refresh()
        
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write(f'GAME OVER!', align='center',  font=FONT)