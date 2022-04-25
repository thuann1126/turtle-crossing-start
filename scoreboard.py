
from turtle import Turtle
from player import Player

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.setposition(-280, 250)

    def scoreUpdate(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="left", font=FONT)

    def scoreIncrease(self):
        self.score += 1

    def gameover(self):
        self.goto(-80, 0)
        self.write("Game Over", False, align="left", font=FONT)

