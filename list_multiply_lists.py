#!/usr/env/bin python3

def multiply_list(l1,l2):
    result = []
    for i in range(len(l1)):
        result.append(l1[i]*l2[i])
    return result


a = [2,4,5]
b = [2,3,6]

print(multiply_list(a,b))
