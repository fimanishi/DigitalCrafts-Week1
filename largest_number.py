#!/usr/env/bin python3

def largest_number(l):
    largest = l[0]
    for i in l:
        if i > largest:
            largest = i
    return largest

print(largest_number([1,2,3,4,8]))
