import time
from turtle import Screen
from random import random

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

window = Screen()
window.setup(width=600, height=600)
window.tracer(0)
window.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



window.onkeypress(player.move, key='Up')
window.onkeypress(player.move, key='w')

def exit():
    global game_is_on
    game_is_on = False
window.onkeypress(exit, key='Escape')


game_is_on = True
while game_is_on:
    
    if car_manager.ckeck_collision(player.ycor()):
        game_is_on = False
        window.update()
        scoreboard.game_over()
        break
        
        
    car_manager.move()
    
    if player.crossed_finish():
        scoreboard.level_up()
        car_manager.increase_speed()
        player.goto_start()
        
    if random() > 0.833 : 
        car_manager.add_car()
        
    time.sleep(0.1)
    window.update()
    
window.exitonclick()