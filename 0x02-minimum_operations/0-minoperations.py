#!/usr/bin/python3
"""Calculates the minimum number of operations to achieve n characters in a string"""


def minOperations(n):
    """Function that returns the minimum number of operations to
    achieve n characters"""
    my_str = "H"
    count = 0

    if n <= 1:
        return 1
    while (len(my_str) < n):
        cpy = copyAll(my_str)

        if (len(my_str) / 2 < n):
            cpy = copyAll(my_str)
            my_str = paste(my_str, cpy)
            count += 1
        else:
            my_str = paste(my_str, cpy)
            count += 1
    if (len(my_str) >= n):
        return count
    return (0)

def copyAll(str):
    """Creates a copy of str"""
    str_cpy = ""
    for c in str:
        str_cpy.join(c)
    return str_cpy

def paste(str1, str2):
    """Concatenates two strings"""
    return str1 + str2