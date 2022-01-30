
from turtle import Screen
from score_level import ScoreLevel
from game_boy import GameBoy
from car_manager import CarManager
from random import choice, randint
import time

Screen().setup(width=600, height=600)
Screen().tracer(0)

cm = CarManager()
sl = ScoreLevel()
gb = GameBoy()

Screen().listen()
Screen().onkey(fun=gb.go_up, key='Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    Screen().update()
    cm.create_car()
    cm.move_cars()

    # detect collision with car
    for car in cm.all_cars:
        if car.distance(gb) < 20:
            game_is_on = False
            sl.write_game_over()

    # detect if the player as crossed to the other side
    if gb.gb_has_crossed():
        sl.increase_level()
        cm.increase_car_speed()
        gb.go_to_beginning()


Screen().exitonclick()

