#!/usr/bin/env python3
"""Module that defines a full Rectangle class based on BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width: the width of the rectangle (integer greater than 0).
            height: the height of the rectangle (integer greater than 0).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
