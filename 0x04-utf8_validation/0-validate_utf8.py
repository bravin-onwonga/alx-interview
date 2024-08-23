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

    len_bin_lst = len(bin_lst)

    if (bin_lst[0][0] == '0'):
        more_than_one = False
    else:
        more_than_one = True
        idx = 0
        bin = bin_lst[0]
        while bin[idx] == '1':
            idx += 1
        if idx > 4:
            return False
        if idx != len_bin_lst:
            return False

    idx = 0
    if more_than_one:
        idx = 1

    while idx < len_bin_lst:
        bin = bin_lst[idx]

        if more_than_one:
            if bin[0] != '1' and bin[2] != 0:
                return False
        else:
            if bin[0] == '1':
                return False
        idx += 1
    return True
