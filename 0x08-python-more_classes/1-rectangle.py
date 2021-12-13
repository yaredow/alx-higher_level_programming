#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        """initialize a rectangle
        Args: 
        width: width of a rectangle
        height: height of a rectangle
        """
        self.height = height
        self.width = width

    def width(self):
        """The property of a rectangle
        Returns: width
        """
        return self.width

    def height(self):
        """The property of a rectangle one side of a rectangle
        Returns: height of a rectangle
        """
        return self.height

    def width(self, value):
        """set the width
        Args:
            value: to set the width to
        Raises:
            TypeError: if width is not int
            ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """the property of height as another side of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height
        Args:
            value: to set the height to
        Raises:
            TypeError: if value is not int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value



