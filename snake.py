from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]

    def create_snake(self):
        self.snake_seg = []
        for pos in STARTING_POSITIONS:
            tim = Turtle(shape="square")
            tim.penup()
            tim.goto(pos)
            tim.color("White")
            self.snake_seg.append(tim)

    def add_snake_seg(self):
        tim = Turtle(shape="square")
        tim.color("White")
        tim.penup()
        self.snake_seg.append(tim)

    def move(self):
        for tims in range(len(self.snake_seg) - 1, 0, -1):
            self.snake_seg[tims].goto(self.snake_seg[tims - 1].xcor(), self.snake_seg[tims - 1].ycor())
        self.head.forward(20)

    def move_up(self):
        if self.snake_seg[0].heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.snake_seg[0].heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.snake_seg[0].heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.snake_seg[0].heading() != 180:
            self.head.setheading(0)

    def new_snake(self):
        for segs in self.snake_seg:
            segs.goto(1000, 1000)
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]



