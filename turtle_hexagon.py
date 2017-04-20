#!/usr/bin/env python3

from turtle import *

def hexagon(size):
    for x in range(6):
        forward(size)
        right(60)

if __name__ == "__main__":
    hexagon(100)
    mainloop()
