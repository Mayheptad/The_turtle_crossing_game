
from turtle import Turtle

GAME_BOY_STARTING_POS = (0, -280)
GAME_BOY_MOVE_DISTANCE = 10
FINISH_LINE_Y_AXIS = 280


class GameBoy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_beginning()

    def go_up(self):
        self.forward(GAME_BOY_MOVE_DISTANCE)

    def gb_has_crossed(self):
        return self.ycor() > FINISH_LINE_Y_AXIS

    def go_to_beginning(self):
        self.goto(GAME_BOY_STARTING_POS)


        
