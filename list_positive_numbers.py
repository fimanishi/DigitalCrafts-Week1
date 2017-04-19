#!/usr/env/bin python3

def positive_numbers(l):
    positive = []
    for i in l:
        if i > 0:
            positive.append(i)
    return positive

print(positive_numbers([1,3,-5,8,-10,25,0,44,-11,64]))
