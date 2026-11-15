#!/usr/bin/env python3
"""Module that defines a Square class with its own string form."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of the square (integer greater than 0).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
