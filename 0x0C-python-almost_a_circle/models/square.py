#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Our Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of Square """
        return "[Square] ({}) {}/{} \
- {}".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the Square object with new values """
        if args is not None and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ Method that returns the dictionary representation """
        attrs = ['id', 'size', 'x', 'y']
        dict = {}
        for key in attrs:
            dict[key] = getattr(self, key)
        return dict
