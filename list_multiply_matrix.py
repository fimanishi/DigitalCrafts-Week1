#!/usr/bin/env python3

def change_second_matrix(m2):
    m2n = []
    length1 = range(len(m2))
    length2 = range(len(m2[0]))
    for i in length2:
        new_line = []
        for j in length1:
            new_line.append(m2[j][i])
        m2n.append(new_line)
    return m2n


def multiply_matrix_one_row(m1, m2):
    tsum = 0
    for i in range(len(m1)):
        tsum += m1[i]*m2[i]
    return tsum

test = []

m1 = [[0,3,5],[5,5,2]]
m2 = [[3,4],[3,-2],[4,-2]]

def multiply_matrix(m1, m2):
    if len(m1[0]) != len(m2):
        print("These matrices can't be multiplied")
        return 0
    m2n = change_second_matrix(m2)
    product = []
    length1 = range(len(m1))
    length2 = range(len(m2n))
    for i in length1:
        line = []
        for j in length2:
            value = multiply_matrix_one_row(m1[i], m2n[j])
            line.append(value)
        product.append(line)
    return product

print(multiply_matrix(m1, m2))
