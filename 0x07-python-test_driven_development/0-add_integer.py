#!/usr/bin/python3
""" Main Module """


def add_integer(a, b=98):
    """ A funtion that adds 2 numbers """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
