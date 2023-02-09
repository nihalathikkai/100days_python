# #
# Create a snake body
# Move the snake
# Control snake
# detect collision with food
# create scoreboard
# detect collision with wall
# detect collision with body
# #

from turtle import Screen
from time import sleep

from snake import Snake
from food import Food
from scoreboard import Scoreboard

tick = 0.1

window = Screen()

window.setup(width=600, height=600)
window.bgcolor('black')
window.title("Snek Game")
window.tracer(0)
window.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.onkeypress(snake.up, key='w')
window.onkeypress(snake.down, key='s')
window.onkeypress(snake.left, key='a')
window.onkeypress(snake.right, key='d')

game_on = True
def exit():
    global game_on
    if game_on: scoreboard.game_over('You stopped the snake', 'darkgreen')
    game_on = False
window.onkeypress(exit, key='Escape')

while game_on:
    snake.move()    
    
    if snake.head.distance(food) <10:
        food.refresh(positions=snake.get_positions())
        snake.add_segment()
        scoreboard.increase_score()
        
    head_pos = snake.head.pos()
    
    if head_pos[0] > 280 or head_pos[0] <-280 or head_pos[1] > 280 or head_pos[1] <-280:
        scoreboard.game_over('You hit the wall')
        game_on = False
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over('You ate yourself')
            game_on = False
            
    window.update()
    sleep(tick)
    
    
window.exitonclick()