#!/usr/bin/env python3

from turtle import *

def square(size):
    for i in range(4):
        forward(size)
        right(90)

if __name__ == "__main__":
    square(100)
    mainloop()
