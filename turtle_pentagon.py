#!/usr/bin/env python3

from turtle import *

def pentagon(size):
    for x in range(5):
        forward(size)
        right(72)

if __name__ == "__main__":
    pentagon(100)
    mainloop()
