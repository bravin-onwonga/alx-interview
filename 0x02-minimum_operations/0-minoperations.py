#!/usr/bin/python3
"""Calculates the minimum number of operations
to achieve n characters in a string"""


def minOperations(n: int) -> int:
    """Function that returns the minimum number of operations to
    achieve n characters"""
    my_str = "H"
    count = 0


    if n <= 0:
        return 0
    try:
        count = find_operations(my_str, n, count)
        return count
    except BaseException:
        return 0


def copyAll(str: str) -> str:
    """Creates a copy of str"""
    str_cpy = ""
    for c in str:
        str_cpy += c
    return str_cpy

def find_operations(str: str, n: int, count: int) -> int:
    if (len(str) == n):
        return count
    if (len(str) > n):
        return 0
    cpy = copyAll(str)
    str = str + cpy
    str = str + cpy
    return (find_operations(str, n, count + 1))

