#!/usr/bin/env python3
"""Define una clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integer"
            )
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character #."""
        print(self)

    def __str__(self):
        """Return the square representation as a string."""
        result = "\n" * self.__position[1]

        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size

            if i < self.__size - 1:
                result += "\n"

        return result
