#!/usr/bin/python3
"""Main module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherited from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize the Rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of a rectangle."""
        return "{}".format(self.__height * self.__width)

    def __str__(self):
        """Return a string representation of the object."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
