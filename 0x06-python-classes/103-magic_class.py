#!/usr/bin/python3
import math
""" Package providing class 'MagicClass' to replicate bytecod"""
import math


class MagicClass():
    """ Declaration of a class to replicate bytecode """
    def __init__(self, radius=0):
        """ Instantiate a MagicClass object to represent a circle """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Calculates  the area of a circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Calculates the circumference of a circle """
        return 2 * math.pi * self.__radius
