#!/usr/bin/env python3

def smallest_number(l):
    smallest = l[0]
    for i in l:
        if i < smallest:
            smallest = i
    return smallest

print(smallest_number([2,3,4,8]))
