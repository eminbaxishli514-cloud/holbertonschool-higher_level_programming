#!/usr/bin/python3
"""
This module generates Pascal's triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows

    Returns:
        list[list[int]]: Pascal's triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        row = [1]  # first element
        for j in range(1, i):
            # each element is sum of the two above
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # last element
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Test cases
    for n in [5, 1, 0, 10, 100]:
        print(f"n = {n}")
        print(pascal_triangle(n))
