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

    j = len(matrix)
    k = 0
    while (k < j):
        for x in range(0, int(n / 2)):
            for y in range(x, n-x-1):
                tmp = matrix[x][y]

                matrix[x][y] = matrix[y][n-1-x]

                matrix[y][n-1-x] = matrix[n-1-x][n-1-y]

                matrix[n-1-x][n-1-y] = matrix[n-1-y][x]

                matrix[n-1-y][x] = tmp
        k += 1

    return matrix
