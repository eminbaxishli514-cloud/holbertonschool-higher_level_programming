#!/usr/bin/python3
"""Module that defines the MyList class which re-implements sorting manually."""


class MyList(list):
    """Custom list class that can print itself sorted using manual recursion."""

    def _quicksort(self, data):
        """Recursive quicksort implementation (no imports, no built-ins)."""
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
        """Print the list sorted using the custom quicksort algorithm."""
        sorted_list = self._quicksort(self[:])
        print(sorted_list)
