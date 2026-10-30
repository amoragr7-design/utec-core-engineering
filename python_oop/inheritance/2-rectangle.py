#!/usr/bin/env python3
"""Defines a Rectangle class with area and string representation."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
