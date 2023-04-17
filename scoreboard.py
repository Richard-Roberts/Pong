from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 230)
        self.write(f"{self.p1_score} : {self.p2_score}", align="center", font=("Arial", 24, "normal"))

    def update_p1_score(self):
        self.clear()
        self.p1_score += 1
        self.write(f"{self.p1_score} : {self.p2_score}", align="center", font=("Arial", 24, "normal"))

    def update_p2_score(self):
        self.clear()
        self.p2_score += 1
        self.write(f"{self.p1_score} : {self.p2_score}", align="center", font=("Arial", 24, "normal"))