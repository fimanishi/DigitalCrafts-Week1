#!/usr/bin/env python3

from turtle import *

def triangle(size):
    for x in range(3):
        forward(size)
        right(120)

if __name__ == "__main__":
    triangle(100)
    mainloop()
