#!/usr/env/bin python3

def multiply_list(l,f):
    for i in range(len(l)):
        l[i] = l[i]*f


a = [1,2,3,4,5]

multiply_list(a,3)

print(a)
