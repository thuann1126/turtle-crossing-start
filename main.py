import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

car_list = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Objects initialize
pler = Player()
sb = Scoreboard()
sb.scoreUpdate()

# Set up the cars
yposition = -240
for _ in range(0, 9):
    car = CarManager(yposition)
    car_list.append(car)
    yposition += 60

# Screen events listener
screen.listen()
screen.onkey(pler.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_list:
        if car.isCollision(pler.xcor(), pler.ycor()):
            sb.gameover()
            game_is_on = False
        car.carMove()
    if pler.ycor() == 280:
        sb.scoreIncrease()
        sb.scoreUpdate()
        for car in car_list:
            car.levelup()
        pler.move()

screen.exitonclick()




