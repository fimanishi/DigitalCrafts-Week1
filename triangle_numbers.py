#!/usr/bin/env python3

def triangle_numbers(number):
    numbers_list = []
    previous = 0
    for i in range(number):
        numbers_list.append(previous+(i+1))
        previous += i+1
    return numbers_list

print(triangle_numbers(10))
