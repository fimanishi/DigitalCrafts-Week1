#!/usr/bin/env python3

def remove_duplicates(l):
    for i in l:
        counter = 0
        for j in l:
            if i == j:
                counter += 1
        if counter > 1:
            l.pop(l.index(i))


a = [1,2,3,4,1,2,6,7]

remove_duplicates(a)

print(a)
