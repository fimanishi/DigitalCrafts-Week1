#!/usr/bin/env python3

from turtle import *

def star(size):
    for x in range(5):
        begin_fill()
        forward(size)
        right(144)
        end_fill()

if __name__ == "__main__":
    star(100)
    mainloop()
