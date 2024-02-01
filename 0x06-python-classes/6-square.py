#!/usr/bin/python3
"""Main module."""


class Square:
    """Class Square that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square class."""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @property
    def position(self):
        """Getter for the position of the square."""
        return self.__position

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

    @position.setter
    def position(self, new_pos):
        """Change the position of the square."""
        if not isinstance(new_pos, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(new_pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(new_pos[0], int) and isinstance(new_pos[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif new_pos[0] < 0 or new_pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = new_pos

    def my_print(self):
        """Print out the square in #."""
        if self.__size is 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for i in range(self.__size):
                    for m in range(self.__position[0]):
                        print(" ", end="")
                    print("#", end="")
                print()
