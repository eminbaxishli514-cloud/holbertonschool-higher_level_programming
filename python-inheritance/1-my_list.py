#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """Class that inherits from list."""

    def __init__(self, iterable=None):
        """Initialize the MyList instance using the parent list."""
        if iterable is None:
            iterable = []
        super().__init__(iterable)

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
