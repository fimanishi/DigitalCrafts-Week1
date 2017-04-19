#!/usr/env/bin python3

def even_numbers(l):
    for i in l:
        if i%2 == 0:
            print(i)

even_numbers([1,3,5,8,10,25,2,44,11,64])
