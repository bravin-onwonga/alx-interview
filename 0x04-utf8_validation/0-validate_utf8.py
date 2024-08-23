#!/usr/bin/python3
"""Utf validation"""


def validUTF8(data):
    """Checks whether the data passed to the fucntion is
    a valid UTF-8 encoding
    Returns:
        True - if is valid
        False - not valid
    """

    for num in data:
        bin = '{0:08b}'.format(num)
        if bin[0] == '0':
            continue
        else:
            idx = 0
            while bin[idx] == '1':
                idx += 1
            if idx > 3:
                return False
    return True
