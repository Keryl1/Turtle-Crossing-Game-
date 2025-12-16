import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle_p = Player()
screen.onkeypress(turtle_p.move_up, "Up")
screen.onkeypress(turtle_p.move_down, "Down")
car = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 5) == 1:
        car.generate_car()
    if turtle_p.ycor() > 210:
        turtle_p.reset_pos()
        scoreboard.new_level()
        car.increase_speed()
    for cars in car.car[:]:
        if turtle_p.distance(cars) < 25:
            scoreboard.game_over()
            game_is_on = False










    car.move()

screen.exitonclick()




























