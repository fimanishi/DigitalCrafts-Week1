#!/usr/env/bin python3

def add_matrix(m1, m2):
    final = []
    for i in range(len(m1)):
        temp = []
        for j in range(len(m1[0])):
            temp.append(m1[i][j]+m2[i][j])
        final.append(temp)
    return final

a = [[1,3],[2,4]]
b = [[5,2],[1,0]]

print(add_matrix(a,b))
