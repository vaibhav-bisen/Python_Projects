from turtle import Turtle


class Boarder(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, -280)
        self.pd()
        self.color("red")
        for _ in range(4):
            self.fd(280 * 2)
            self.left(90)
