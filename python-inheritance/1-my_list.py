#!/usr/bin/python3
"""Module that defines the MyList class with custom sorting."""


class MyList(list):
    """A class that inherits from list and prints a sorted version."""

    def _custom_sort(self, items):
        """Sort items using a manual recursive algorithm."""
        if len(items) < 2:
            return items

        pivot = items[0]
        left = []
        right = []

        for value in items[1:]:
            if value < pivot:
                left.append(value)
            else:
                right.append(value)

        return self._custom_sort(left) + [pivot] + self._custom_sort(right)

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        sorted_list = self._custom_sort(self[:])
        print(sorted_list)
