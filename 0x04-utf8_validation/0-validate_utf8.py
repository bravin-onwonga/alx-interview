#!/usr/bin/python3
"""Utf validation"""


def validUTF8(data):
    """Checks whether the data passed to the fucntion is
    a valid UTF-8 encoding
    Returns:
        True - if is valid
        False - not valid
    """
    for code in data:
        if code > 128 or code < 1:
            return False
        return True
