#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
