import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim=Player()
car=CarManager()

screen.listen()
screen.onkey(tim.go_up,"Up")
level=0
#screen.onkey(tim.go_down,"Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars(level)
    for i in range(len(car.all_cars)):
        if tim.distance(car.all_cars[i])<20:
            print("gameover")
            game_is_on=False
    if tim.ycor()>=280:
        level=level+1
        print(level+1)
        tim.goto(0,-280)



screen.exitonclick()