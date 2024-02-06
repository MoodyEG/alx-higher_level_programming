#!/usr/bin/python3
"""Main module."""


class Student:
    """Class Student that defines a Student's info."""
    def __init__(self, first_name, last_name, age):
        """Initialize the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A function retrieves a dictionary
        representation of a Student instance """
        if attrs:
            disl = {}
            for i in range(len(attrs)):
                for j in self.__dict__:
                    if attrs[i] == j:
                        disl[j] = self.__dict__[j]
            return disl

        return self.__dict__
