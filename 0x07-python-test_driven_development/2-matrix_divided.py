#!/usr/bin/python3
""" Main Module """


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix """
    msg_t = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_t)
    ln = 0
    for lists in matrix:
        if not lists or not isinstance(lists, list):
            raise TypeError(msg_t)
        if ln != 0 and len(lists) != ln:
            msg_l = "Each row of the matrix must have the same size"
            raise TypeError(msg_l)
        for num in lists:
            if not type(num) in (int, float):
                raise TypeError(msg_t)
        ln = len(lists)
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
