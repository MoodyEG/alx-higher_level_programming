#!/usr/bin/python3
"""Main module."""


class Square:
    """Class Square that defines a square."""
    def __init__(self, size=0):
        """Initialize the Square class."""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Set a new value for the size attribute."""
        if isinstance(new_size, int):
            if new_size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = new_size
        else:
            raise TypeError("size must be an integer")
