#!/usr/bin/python3
"""
Module for pickling and unpickling a custom Python object.
"""

import pickle


class CustomObject:
    """
    A custom Python class with attributes name, age, and is_student.

    Methods:
        display(): Prints the object's attributes.
        serialize(filename): Serializes the object to a file using pickle.
        deserialize(cls, filename): Class method to load object from pickle file.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """
        Serialize the current object instance to a file using pickle.

        Args:
            filename (str): The file where the object will be saved.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a pickle file into a CustomObject instance.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError):
            return None
