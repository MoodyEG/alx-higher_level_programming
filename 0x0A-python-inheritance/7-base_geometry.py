#!/usr/bin/python3
"""Main module."""


class BaseGeometry:
    """Not an empty class anymore"""
    def area(self):
        """Raises an excpetion"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
