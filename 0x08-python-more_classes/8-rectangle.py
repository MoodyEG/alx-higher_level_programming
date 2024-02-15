#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Class to defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        form += (str(self.print_symbol) * self.width + "\n") * self.height
        return form[:-1]

    def __repr__(self):
        """ Representation of Rectangle object """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ When the rectangle is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
