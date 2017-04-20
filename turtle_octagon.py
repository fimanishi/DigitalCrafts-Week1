#!/usr/bin/env python3

from turtle import *

def octagon(size):
    pencolor("black")
    fillcolor("red")
    begin_fill()
    for x in range(8):
        forward(size)
        right(45)
    end_fill()

if __name__ == "__main__":
    octagon(100)
    mainloop()
