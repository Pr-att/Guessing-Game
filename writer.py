from turtle import *


class New(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.hideturtle()