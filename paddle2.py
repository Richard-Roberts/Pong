from turtle import Turtle


class Paddle2(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.paddle_position = 0
        self.goto(240, self.paddle_position)
        self.up = True
        self.setheading(90)
        self.shapesize(1, 3, 0)
        self.speed("fast")

    def move(self):
        if self.up:
            self.forward(10)
            if self.ycor() >= 270:
                self.up = False
        else:
            self.backward(10)
            if self.ycor() <= -270:
                self.up = True

    def update(self):
        self.paddle_position = 0
        self.goto(240, self.paddle_position)
        self.up = True
        self.setheading(90)