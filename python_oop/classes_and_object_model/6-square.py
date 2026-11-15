#!/usr/bin/env python3
"""Module that defines a Square class with size, position and a string form."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.

        Args:
            size: the size of the square (integer >= 0).
            position: tuple of 2 positive integers (spaces, lines).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: the new size (integer >= 0).

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        message = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(message)
        for item in value:
            if not isinstance(item, int) or item < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #."""
        print(str(self))

    def __str__(self):
        """Return the square drawn with # as a string."""
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        rows = "\n".join([row] * self.__size)
        return "\n" * self.__position[1] + rows
