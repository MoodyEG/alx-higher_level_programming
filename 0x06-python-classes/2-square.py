#!/usr/bin/python3
"""Main module."""


class Square:
    """Class Square that defines a square."""
    def __init__(self, size=0):
        """Initialize the Square class."""
        if size is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
