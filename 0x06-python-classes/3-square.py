#!/usr/bin/python3
""" definition of a class 'Square'
"""


class Square():
    """ Definition of 'Square'
    """
    def __init__(self, size=0):
        """ Instance of 'Square'
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Finds the area of the square
        """
        return self.__size * self.__size
