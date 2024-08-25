#!/usr/bin/python3
"""Utf validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Checks whether the data passed to the fucntion is
    a valid UTF-8 encoding
    Returns:
        True - if is valid
        False - not valid
    """
    bin_lst = []

    for num in data:
        bin_lst.append(num_to_bin(num))

    idx = 0
    n = 0

    return check_bin(bin_lst, idx, n)


def num_to_bin(num: int) -> str:
    """Converts an interger to its binary rep"""
    str = ''

    str += '{0:08b}'.format(num)

    len_str = len(str)

    if len_str == 8:
        return (str)
    else:
        str2 = ""
        count = 0
        idx = len_str - 1
        while (count < 8):
            str2 += str[idx]
            idx -= 1
            count += 1
        return (str2)


def check_bin(my_lst: List[str], idx: int, n: int) -> bool:
    """Recursively checks if the binary number is UTF-8 valid
    Returns:
        True - UTF-8 Valid
        False - Not valid
    """
    if (idx == len(my_lst)):
        return True

    if (n == 0 and my_lst[idx][0] == '0'):
        return check_bin(my_lst, idx + 1, n)

    if my_lst[idx][0] == '1' and n > 0:
        num = int(my_lst[idx], 2)
        if num >> 6 != 2:
            return False
        else:
            if (n):
                n -= 1
            return check_bin(my_lst, idx + 1, n)

    if my_lst[idx] == '1' and n == 0:
        i = 0
        while [my_lst[idx][i] == '1']:
            i += 1
        n = i
        if n == 1:
            num = int(my_lst[idx], 2)
            if num >> 6 != 2:
                return False
            n -= 1
        return check_bin(my_lst, idx + 1, n)

    return False
