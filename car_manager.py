import random
from turtle import Turtle
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVEMENT_SPEED = [10, 15, 20, 25, 30]
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self, y):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random.randint(0, 5)])
        self.penup()
        self.shapesize(1, 2)
        self.yposition = y
        self.randomspeed = MOVEMENT_SPEED[random.randint(0, 4)]
        self.goto(250, self.yposition)
        self.setheading(180)



    def carMove(self):
        if self.xcor() > -300:
            self.forward(self.randomspeed)
        else:
            self.goto(250, self.yposition)

    def isCollision(self, x_player, y_player):
        if self.xcor() <= x_player + 10 and self.xcor() >= x_player - 10 and self.ycor() <= y_player + 10 and self.ycor() >= y_player -10:
            return True
        else:
            return False

    def levelup(self):
        self.randomspeed += MOVE_INCREMENT






