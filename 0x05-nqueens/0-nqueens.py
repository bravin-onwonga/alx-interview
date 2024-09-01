#!/usr/bin/python3
""" N queens """
import sys
from typing import List


"""
Initialize my chess board
Fill the beginning box with one
Fill all unfit boxes with zero
Go to the next row
If I can't fill that row check if the previous row has a free slot
If not use another beginning point
If you can fill that row countinue
append the box to lst
If you have made n entries return lst

"""


""" def remove_spaces(lst, box, n):
    row = lst[box[0]]
    i = 0
    for i in range(len(row)):
        if row[i] != 1:
            row[i] = 0

    diagonals = find_all_diags(box, n)

    for diagonal in diagonals:
        row = diagonal[0]
        col = diagonal[1]

        lst[row][col] = " "

    return lst """


def fill_spaces(lst: List[List], box: List[int], n: int) -> List[List]:
    """ Fills unfit spaces with zero """
    row = lst[box[0]]
    i = 0
    for i in range(len(row)):
        if row[i] != 1:
            row[i] = 0

    diagonals = find_all_diags(box, n)

    for diagonal in diagonals:
        row = diagonal[0]
        col = diagonal[1]

        lst[row][col] = 0

    return lst


def find_all_diags(box: List[int], n: int) -> List[List]:
    diagonals = []

    row = box[0]
    col = box[1]

    k = row + 1
    j = col + 1

    while (k < n and j < n):
        diagonals.append([k, j])
        k += 1
        j += 1

    k = row - 1
    j = col - 1

    while (k >= 0 and j >= 0):
        diagonals.append([k, j])
        k -= 1
        j -= 1

    k = row - 1
    j = col + 1

    while (k >= 0 and j < n):
        diagonals.append([k, j])
        k -= 1
        j += 1

    k = row + 1
    j = col - 1

    while (k < n and j >= 0):
        diagonals.append([k, j])
        k += 1
        j -= 1

    return diagonals


def make_entries(board: List[List], entries: int, n: int, lst: List[List], box: List[int]) -> List[List]:
    if entries == n:
        return (lst, entries)

    board = fill_spaces(board, box, n)

    lst.append(box)
    entries += 1

    row_idx = box[0] + 1

    if row_idx >= n:
        return (lst, entries)

    row = board[row_idx]

    print(row)

    for i in range(len(row)):
        if row[i] == " ":
            row[i] = 1
            lst.append([row_idx, i])
            print(lst)
            return make_entries(board, entries + 1, n, lst, [row_idx, i])
    return (lst, entries)


def n_queens(n: int) -> None:
    """Fit many queens on a board
    without them attacking each other"""
    board = []
    row = []
    res = []

    for i in range(n):
        for j in range(n):
            row.append(" ")
        board.append(row)

    tries = 0

    while (tries < n):
        entries = 0
        board[0][tries] = 1
        entries += 1
        lst = []
        lst, entries = make_entries(board, entries, n, lst, [0, entries])
        if entries == n:
            res.append(lst)
        entries = 0
        board = []
        for i in range(n):
            board.append(row)
        tries += 1

    print(res)


if __name__ == '__main__':
    n = int(sys.argv[1])
    n_queens(n)
