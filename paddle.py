from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.paddle_position = 0
        self.goto(-240, self.paddle_position)
        self.setheading(90)
        self.shapesize(1, 3, 0)
        self.speed("fast")

    def move_down(self):
        if self.paddle_position != -300:
            self.backward(10)

    def move_up(self):
        if self.paddle_position != 300:
            self.forward(10)

    def update(self):
        self.paddle_position = 0
        self.goto(-240, self.paddle_position)
        self.setheading(90)
