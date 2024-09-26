#!/usr/bin/python3
"""
Handling list (2D Matrix)
"""

from typing import List


def check_cells(grid: List[List[int]], i: int, j: int) -> int:
    """ Calculates the perimeter of a cell
    Params:
        grid - 2D matrix
        i - row index
        j - column index
    Returns:
        perimeter of cell
        whether to start or stop """
    cell_perimeter = 0

    # top
    if i == 0 or grid[i - 1][j] == 0:
        cell_perimeter += 1

    # left
    if j == 0 or grid[i][j - 1] == 0:
        cell_perimeter += 1

    # right
    if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
        cell_perimeter += 1

    # bottom
    if i == len(grid) - 1 or grid[i + 1][j] == 0:
        cell_perimeter += 1
    return cell_perimeter


def island_perimeter(grid: List[List[int]]) -> int:
    """ Calculates the perimeter of an island
    Params:
        grid - a list of list of integers:
    0 represents water
    1 represents land
    Returns:
        perimeter of the island """
    perimeter = 0

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                num = check_cells(grid, i, j)
                perimeter += num
    return perimeter
