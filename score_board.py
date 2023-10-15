from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as highscore:
            score = int(highscore.read())
        self.high_score = score
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.write(arg=f"SCORE : {self.score}   HIGH SCORE : {self.high_score}", align="center", font=("Arial", 20,
                                                                                                       "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"SCORE : {self.score}   HIGH SCORE : {self.high_score}", align="center", font=("Arial", 20,
                                                                                                       "normal"))
        with open("high_score.txt", mode="w") as highscore:
            highscore.write(f"{self.high_score}")

    def game_stop(self):
        self.clear()
        self.goto(0, 0)
        self.color("White")
        self.write(arg="GAME STOPPED", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.clear()
        self.write(arg=f"SCORE : {self.score}   HIGH SCORE : {self.high_score}", align="center", font=("Arial", 20,
                                                                                                       "normal"))
        with open("high_score.txt", mode="w") as highscore:
            highscore.write(f"{self.high_score}")


