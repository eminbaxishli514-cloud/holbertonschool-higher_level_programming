#!/usr/bin/python3

class Student:
    """Student class with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary of the student’s attributes.

        If attrs is a list, only include those keys that exist.
        """
        if attrs is None:
            return self.__dict__.copy()

        result = {}
        for key in attrs:
            if key in self.__dict__:
                result[key] = self.__dict__[key]
        return result
