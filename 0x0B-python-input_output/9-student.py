#!/usr/bin/python3
"""Main module."""


class Student:
    """Class Student that defines a Student's info."""
    def __init__(self, first_name, last_name, age):
        """Initialize the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A function retrieves a dictionary
        representation of a Student instance """
        return self.__dict__
