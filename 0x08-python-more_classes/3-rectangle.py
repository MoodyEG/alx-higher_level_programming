#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Class to defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes the Rectangle """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @width.setter
    def width(self, value):
        """ Width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculates the area """
        return self.height * self.width

    def perimeter(self):
        """ Calculates the perimeter """
        return 2 * (self.height + self.width)

    def __str__(self):
        """ Display the rectangle in # form """
        form = ""
        if self.width == 0 or self.height == 0:
            return form
        form += ("#" * self.width + "\n") * self.height
        return form[:-1]
