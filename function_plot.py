#!/usr/bin/env python3

import matplotlib.pyplot as plot
import math
from numpy import arange
from degree_conversion import to_farenheit

def f(x):
    return x+1

def x_range(low,high):
    xs = arange(low,high)
    return xs

def squaref(x):
    return pow(x, 2)

def odds(x):
    if x%2 == 1:
        return 1
    else:
        return -1

def plot_sin(x):
    return math.sin(x)

def main():
    xs = x_range(0,100)
    ys = []

    for x in xs:
        ys.append(to_farenheit(x))

    plot.plot(xs, ys)
    plot.show()

if __name__ == "__main__":
    main()
