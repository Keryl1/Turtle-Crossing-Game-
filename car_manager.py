from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.car = []


    def generate_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_x_cord = 300
        new_y_cord = random.randint(-210, 210)
        new_car.goto(new_x_cord, new_y_cord)

        self.car.append(new_car)

    def move(self):
        for item in range(len(self.car)):
            self.car[item].backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT







































