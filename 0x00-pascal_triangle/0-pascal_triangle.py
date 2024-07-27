#!/usr/bin/python3
"""Creates a pascals triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]
        for j in range(1, len(prev_row)):
            if (j < len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
