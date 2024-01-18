#!/usr/bin/python3

""" Library providing a definition of a class 'Square'
"""


class Square():
    """ Declaration of a 'Square'
    """
    def __init__(self, size=0):
        """ Create an instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be an integer")
        self.__size = size
