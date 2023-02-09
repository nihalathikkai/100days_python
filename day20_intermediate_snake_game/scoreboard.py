from turtle import Turtle

FONT = ('Consolas',14,'bold')
ALIGNMENT = "center"
DATA_FILE_PATH = "/python/100days/day20_intermediate_snake_game/data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.score = 0
        try:
            with open(DATA_FILE_PATH, 'r') as file:
                self.high_score = int(file.readline().strip())
        except:
            self.high_score = 0
        
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}  |  Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self, msg:str, color:str='red'):
        self.color(color)
        self.goto(0,20)
        self.write(msg, align=ALIGNMENT, font=FONT)
        self.goto(0,0)
        self.write(f"GAME OVER!! Your score is {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0,-280)
        self.color('darkcyan')
        self.write("Click on screen to close the game.", align=ALIGNMENT, font=FONT)
        
        if self.score > self.high_score:
            with open(DATA_FILE_PATH, 'w') as file:
                file.write(str(self.score))