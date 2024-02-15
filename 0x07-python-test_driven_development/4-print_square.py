#!/usr/bin/python3
""" Main Module """


def print_square(size):
    """ A  function that print a square with the character # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
