import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from paddle2 import Paddle2
from middle import Middle
from ball import Ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle()
paddle2 = Paddle2()
middle = Middle()
ball = Ball()


screen.listen()
screen.onkeypress(paddle.move_down, "Down")
screen.onkeypress(paddle.move_up, "Up")


def play():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.05)
        paddle2.move()
        ball.move()

        if ball.distance(paddle) <= 20:
            print("touching")
            print(ball.heading())
            heading = ball.heading() + 180
            if heading > 360:
                heading -= 360
            ball.gogo = heading
            print(ball.heading())

        if ball.distance(paddle2) <= 20:
            print("touching")
            print(ball.heading())
            heading = ball.heading() + 180
            if heading > 360:
                heading -= 360
            ball.gogo = heading
            print(ball.heading())

        if ball.xcor() <= -300:
            scoreboard.update_p2_score()
            ball.update()
            paddle.update()
            paddle2.update()

        if ball.xcor() >= 300:
            scoreboard.update_p1_score()
            ball.update()
            paddle.update()
            paddle2.update()



play()

screen.exitonclick()
