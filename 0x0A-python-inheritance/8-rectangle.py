#!/usr/bin/python3
"""Defines class Rectangle which inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry




class Rectangle(BaseGeometry):
    """Represent a class to define rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a Rectangle.
        Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.
        """

        def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
