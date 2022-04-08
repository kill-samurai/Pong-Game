from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game!")
screen.listen()
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
screen.onkey(fun=player_1.move_up, key="w")
screen.onkey(fun=player_1.move_down, key="s")
screen.onkey(fun=player_2.move_up, key="Up")
screen.onkey(fun=player_2.move_down, key="Down")

ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when player 2 misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.player_2_scores()

    # Detect when player 1 misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.player_1_scores()































screen.exitonclick()
