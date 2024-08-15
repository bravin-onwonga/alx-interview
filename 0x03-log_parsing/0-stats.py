#!/usr/bin/python3
"""Module to parse data into a particular format
Print after 10 lines are read and/or after CTRL-C is pressed
"""

import sys
import signal

total_size = 0
count = 0
status_codes = {}


def print_logs(status_codes: dict, total_size: int) -> None:
    """Prints the logs passed
    Print after 10 lines are read and/or after CTRL-C is pressed
    Status codes are sorted"""
    print(f'File size: {total_size}')
    codes = list(status_codes.keys())
    codes.sort()
    sorted_dict = {i: status_codes[i] for i in codes}
    for code, num in sorted_dict.items():
        print(f'{code}: {num}')


for line in sys.stdin:
    """Loops through stdinput until CTRL-C is pressed
    Returns nothing
    """
    n = 10
    my_lst = line.split(" ")
    status_code = my_lst[-2]
    if status_codes.get(status_code):
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1
    file_size = int(my_lst[-1])
    total_size += file_size
    count += 1
    if count == 10:
        print_logs(status_codes, total_size)
        count = 0

signal.signal(signal.SIGINT)
