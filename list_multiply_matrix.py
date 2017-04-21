#!/usr/bin/env python3


# matrix transpose
def transpose_second_matrix(m2):
    m2n = []
    # takes the number of rows
    length1 = range(len(m2))
    # takes the number of columns
    length2 = range(len(m2[0]))
    for i in length2:
        new_line = []
        for j in length1:
            # gets all the elements from the jth column and add to a new list
            new_line.append(m2[j][i])
        # appends the list of columns items as a row
        m2n.append(new_line)
    return m2n

# multiply one row matrices
def multiply_matrix_one_row(m1, m2):
    tsum = 0
    # goes through all items on the row, multiply with the correspondent item on the other matrix and add the result
    for i in range(len(m1)):
        tsum += m1[i]*m2[i]
    return tsum

# multiply matrices as long as the operation is valid

def multiply_matrix(m1, m2):
    # checks if the number of columns in the first matrix is equal to the number of rows in the second matrix
    if len(m1[0]) != len(m2):
        print("These matrices can't be multiplied")
        return 0
    # transpose second matrix
    m2n = transpose_second_matrix(m2)
    # creates the list that will return the result
    product = []
    # gets the number of rows in matrix one and creats a range from zero to it
    length1 = range(len(m1))
    # gets the number of rows in matrix two and creats a range from zero to it
    length2 = range(len(m2n))
    # for each row in matrix one
    for i in length1:
        # creates a temporary new row
        line = []
        # for each row in matrix two
        for j in length2:
            # multiply the ith row in matrix one with the jth row in the transposed matrix two
            value = multiply_matrix_one_row(m1[i], m2n[j])
            # appends that value to the temporary new row
            line.append(value)
        # appends the temporary new row to the final result
        product.append(line)
    return product

if __name__ == "__main__":
    m1 = [[0,3,5],[5,5,2]]
    m2 = [[3,4],[3,-2],[4,-2]]
    print(multiply_matrix(m1, m2))
