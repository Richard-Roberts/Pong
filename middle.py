from turtle import Turtle


class Middle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor("white")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)

        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


