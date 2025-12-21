#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class with an unimplemented area method."""

    def area(self):
        """Raises an Exception with a specific message."""
        raise Exception("area() is not implemented")
