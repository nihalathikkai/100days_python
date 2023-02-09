from turtle import Screen
from time import sleep

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


window = Screen()
window.setup(width=800, height= 600)
window.title('Pong')
window.bgcolor('black')
window.tracer(0)
window.listen()

r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
ball = Ball()
scoreboard = Scoreboard()

window.onkeypress(l_paddle.up, key='w')
window.onkeypress(l_paddle.down, key='s')
window.onkeypress(r_paddle.up, key='Up')
window.onkeypress(r_paddle.down, key='Down')

game_on = True
def exit():
    global game_on
    game_on = False
window.onkeypress(exit, key='Escape')


while game_on:
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
    
    if ball.ycor() > 280 or ball.ycor() < -280 : 
        ball.bounce_y()
        
    if (ball.xcor()>360 and r_paddle.ycor()-50<= ball.ycor()<=r_paddle.ycor()+50) or (ball.xcor()<-360 and l_paddle.ycor()-50<= ball.ycor()<=l_paddle.ycor()+50):
        ball.bounce_x()
        
    ball.move()
    window.update()
    sleep(ball.move_speed)


window.exitonclick()
