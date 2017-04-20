#!/usr/bin/env python3

from turtle import *
from math import pi

def circle(radius):
    for x in range(360):
        forward(2*pi*radius/360)
        right(1)

if __name__ == "__main__":
    circle(50)
    mainloop()
