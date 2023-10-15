import time
from snake import Snake
from food import Food
from turtle import Screen
from score_board import Scoreboard

my_screen = Screen()
my_screen.setup(height=700, width=700)
my_screen.bgcolor("Black")
my_screen.title("The Snake Game")
my_screen.tracer(0)

scoresboard = Scoreboard()
snake = Snake()
s_food = Food()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.move_up)
my_screen.onkey(key="Down", fun=snake.move_down)
my_screen.onkey(key="Left", fun=snake.move_left)
my_screen.onkey(key="Right", fun=snake.move_right)

# def end_game():
#         return False


game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with wall
    if snake.head.xcor() < -330 or snake.head.ycor() < -330 or snake.head.xcor() > 330 or snake.head.ycor() > 330:
        snake.new_snake()
        scoresboard.reset()
        s_food.new_position()

    # Collision with food
    if s_food.food.distance(snake.head) < 15:
        scoresboard.increase_score()
        snake.add_snake_seg()
        s_food.new_position()

    # if my_screen.onkey(key="s", fun=scoresboard.game_stop):
    #     game_is_on = False

    # Collision with self
    for segments in snake.snake_seg[1:]:
        if snake.head.distance(segments) < 10:
            snake.new_snake()
            scoresboard.reset()
            s_food.new_position()

my_screen.exitonclick()
