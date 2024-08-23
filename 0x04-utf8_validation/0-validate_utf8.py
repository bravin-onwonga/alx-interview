#!/usr/bin/python3
"""Utf validation"""


def validUTF8(data):
    """Checks whether the data passed to the fucntion is
    a valid UTF-8 encoding
    Returns:
        True - if is valid
        False - not valid
    """
    bin_lst = []

    for num in data:
        bin_lst.append('{0:08b}'.format(num))
    first_bin = bin_lst[0]

    if first_bin[0] == '0':
        return True
    else:
        idx = 0
        while first_bin[idx] == '1' and idx < 8:
            idx += 1
        while idx < 8:
            if first_bin[idx] == '1':
                return False
            idx += 1
        return True
