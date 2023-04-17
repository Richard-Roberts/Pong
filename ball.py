from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fast")
        self.gogo = 180.0

    def move(self):
        self.setheading(self.gogo)
        self.forward(5)

    def update(self):
        self.goto(0, 0)
        self.gogo = 180
        self.setheading(self.gogo)
        self.forward(5)

