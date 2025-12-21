#!/usr/bin/python3
"""Module for add_attribute function."""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError if the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
