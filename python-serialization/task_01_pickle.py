#!/usr/bin/python3
""" Module for custom object serialization using pickle """
import pickle


class CustomObject:
    """ A custom Python class to demonstrate pickling """
    def __init__(self, name, age, is_instructor):
        self.name = name
        self.age = age
        self.is_instructor = is_instructor

    def display(self):
        """ Prints the object's attributes """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Instructor: {self.is_instructor}")

    def serialize(self, filename):
        """ Serializes the current instance to a file """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """ Loads a serialized instance from a file """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
