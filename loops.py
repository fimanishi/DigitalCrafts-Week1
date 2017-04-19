#!/usr/bin/env python3

from math import ceil

def print_box():
    width = int(input("Width: "))
    height = int(input("Height: "))

    for i in range(height):
        if i == 0 or i == height-1:
            print("*"*width)
        else:
            print("*{}*".format(" "*(width-2)))

def print_triangle(rows):
    spaces = rows - 1
    for i in range(rows):
        print("{}{}".format(" "*spaces, "*"*(1+2*i)))
        spaces -= 1

def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
            print("{} X {} = {}".format(i,j,i*j))
