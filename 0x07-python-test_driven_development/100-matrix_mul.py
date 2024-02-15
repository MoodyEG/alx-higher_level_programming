#!/usr/bin/python3
""" Main module """


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for lists in m_a:
        if not isinstance(lists, list):
            raise TypeError("m_a must be a list of lists")
    for lists in m_b:
        if not isinstance(lists, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    for lists in m_a:
        for elem in lists:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for lists in m_b:
        for elem in lists:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    ln = 0
    for lists in m_a:
        if ln != 0 and ln != len(lists):
            raise TypeError("each row of m_a must be of the same size")
        ln = len(lists)
    ln = 0
    for lists in m_b:
        if ln != 0 and ln != len(lists):
            raise TypeError("each row of m_b must be of the same size")
        ln = len(lists)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        sums = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            sums.append(sum)
        result.append(sums)
    return result
