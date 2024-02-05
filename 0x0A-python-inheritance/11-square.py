#!/usr/bin/python3
"""Main module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""
    def __init__(self, size):
        """Initialize the Square class."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate and return the area of a Square."""
        return "{}".format(self.__size ** 2)

    def __str__(self):
        """Return a string representation of the object."""
        return "[Square] {}/{}".format(self.__size, self.__size)
