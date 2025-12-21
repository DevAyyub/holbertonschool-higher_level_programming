#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """
    Represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
