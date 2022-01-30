
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 10, "normal")


class ScoreLevel(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 270)
        self.write_scores()

    def write_scores(self):
        self.write(f'Level: {self.level}', font=FONT, align='left')

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f'GAME 0VER', font=('Courier', 50, "normal"), align=ALIGNMENT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_scores()
