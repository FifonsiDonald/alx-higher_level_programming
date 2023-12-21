#!/usr/bin/python3
""" Definition of a class 'Square'
"""


class Square():
    """ Calculate the area of a 'Square'
    """
    def __init__(self, size=0):
        """ Instantiate a 'Square'
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Finds the area of a 'Square'
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter method for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
