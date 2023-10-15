import random
from random import randint
from turtle import Turtle


class Food:
    def __init__(self):
        self.food = Turtle(shape="circle")
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.penup()
        self.food.color("blue")
        self.food.goto(randint(-330, 300), randint(-330, 300))

    def new_position(self):
        self.food.goto(randint(-330, 330), randint(-330, 330))
