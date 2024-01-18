#!/usr/bin/python3
""" Class Rectangle that inerits base"""
from models.base import Base



class Rectangle(Base):
	"""Inherits Base and is a rectangle"""
	def __init__(self, width, height, x=0, y=0, id=None):
		"""Class Constructor"""
		super().__init__(id)
		self.width = width
		self.height = height
		self.y = y
		self.x = x

	@property
	def width(self):
		return (self.__width)

	@width.setter
	def width(self, width):
		if type(width) is not int:
			raise TypeError("width must be an integer")
		if width <= 0:
			raise ValueError("width must be > 0")
		self.__width = width
	@property
	def height(self):
		return (self.__height)

	@height.setter
	def height(self, height):
		if type(height) is not int:
                        raise TypeError("height must be an integer")
		if height <= 0:
                        raise ValueError("height must be > 0")
		self.__height = height

	@property
	def x(self):
		return (self.__x)
	@x.setter
	def x(self, x):
		if type(x) is not int:
                        raise TypeError("x must be an integer")
		if x < 0:
			raise ValueError("x must be >= 0")
		self.__x = x 

	@property
	def y(self):
		return(self.__y)
	@y.setter
	def y(self, y):
		if type(y) is not int:
                        raise TypeError("x must be an integer")
		if y < 0:
                        raise ValueError("y must be >= 0")
		self.__y = y
	def area(self):
		"""The area of the rectangle"""
		return (self.__width * self.__height)

	def display(self):
		"""prints in stdout the Rectangle 
		instance with the character #"""
		print("\n" * self.__y, end="")
		print("\n".join([" " * self.__x + "#" * self.__width] * self.__height))
	def __str__:
		"""overriding the __str__ method"""
		return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id)
	def update(self, *args, **kwargs):
		""" assigns an argument to each attribute"""
		if args:
			for i in range(len(args)):
				if i == 0:
					self.id = args[i]
				if i == 1:
					self.__width = args[i]
				if i == 2:
					self.__height = args[i]
				if i == 3:
					self.__x = args[i]
				if i == 4:
					self.__y = args[i]
		else:
			for j, k in kwargs.items():
				seattr(self, j, k)
	def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle"""
        return ({'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y})			
