#!/usr/bin/python3
"""Module that defines the MyList class with a custom sort implementation."""


class MyList(list):
    """Class that inherits from list and prints a manually sorted version."""

    def _quicksort(self, data):
        """Recursive quicksort algorithm implemented manually."""
        if len(data) < 2:
            return data

        pivot = data[0]
        smaller = []
        greater = []

        for x in data[1:]:
            if x > pivot:
                greater.append(x)
            else:
                smaller.append(x)

        return self._quicksort(smaller) + [pivot] + self._quicksort(greater)

    def print_sorted(self):
        """Print a sorted version of the list using the custom quicksort."""
        sorted_copy = self._quicksort(self[:])
        print(sorted_copy)
