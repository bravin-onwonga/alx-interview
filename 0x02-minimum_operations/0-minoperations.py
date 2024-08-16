#!/usr/bin/python3
"""Calculates the minimum number of operations
to achieve n characters in a string"""


def minOperations(n):
    """Function that returns the minimum number of operations to
    achieve n characters"""
    my_str = "H"

    count = 0

    if n <= 1:
        return 1
    try:
        while (len(my_str) < n):
            if (len(my_str) >= n):
                break
            cpy = copyAll(my_str)
            count += 1
            my_str = paste(my_str, cpy)
            count += 1
            if (len(my_str) >= n):
                break
            my_str = paste(my_str, cpy)
            count += 1
            if (len(my_str) >= n):
                break
            if (len(my_str) + len(cpy) >= n):
                my_str = paste(my_str, cpy)
                count += 1
        return count
    except BaseException:
        return 0


def copyAll(str):
    """Creates a copy of str"""
    str_cpy = ""
    for c in str:
        str_cpy += c
    return str_cpy


def paste(str1, str2):
    """Concatenates two strings"""
    new_str = ""
    for c in str1:
        new_str += c
    for c in str2:
        new_str += c
    return new_str
