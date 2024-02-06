""" #!/usr/bin/python3 """
"""Main module."""


def pascal_triangle(n):
    """ A function that returns a list of lists
    of integers representing the Pascal's triangle of n """
    if n <= 0:
        return []
    past = [[] for row in range(n)]
    for i in range(len(past)):
        past[i] = [0]*(i+1)
        past[i][0] = 1
        past[i][i] = 1
        for j in range(1, i):
            past[i][j] = past[i-1][j-1] + past[i-1][j]
    return past
