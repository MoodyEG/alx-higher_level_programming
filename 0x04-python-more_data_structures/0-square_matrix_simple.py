#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    for i in range(len(matrix)):
        sq.append(list(map(lambda x: x**2, matrix[i])))
    return sq
