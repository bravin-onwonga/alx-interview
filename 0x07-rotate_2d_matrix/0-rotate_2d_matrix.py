#!/usr/bin/python3
"""
Simple module to rotate a matrix in place
Focus on reducing the space complexity involved
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix 90 degrees clockwise
    Param:
        matrix - size of an n x n matrix
    Returns:
        Rotated matrix
    """
    n = len(matrix[0])

    if len(matrix) != len(matrix[0]):
        return
    n = len(matrix)
    for i in range(n // 2):
        x, y, slot = i, n - 1 - i, 0
        for i in range(x, y):
            top = matrix[x][i]
            matrix[x][i] = matrix[y - slot][x]
            matrix[y - slot][x] = matrix[y][y - slot]
            matrix[y][y - slot] = matrix[i][y]
            matrix[i][y] = top
            slot += 1
