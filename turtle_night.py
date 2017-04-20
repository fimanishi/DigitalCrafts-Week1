#!/usr/bin/env python3

from turtle import *
from turtle_star import star
from random import randint

bgcolor("black")

color("yellow")

width(10)

for i in range(5):
    star(30)
    up()
    right(randint(0,361))
    forward(randint(100,200))
    down()

mainloop()
