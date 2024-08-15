#!/usr/bin/python3
"""Parsing data into a particular format
Input will be in the form:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

import sys
import signal

total_size: int = 0
count: int = 0
status_codes: dict = {}


def print_logs(status_codes: dict, total_size: int) -> None:
    """Prints the logs passed"""
    print(f'File size: {total_size}')
    codes = list(status_codes.keys())
    codes.sort()
    sorted_dict = {i: status_codes[i] for i in codes}
    for code, num in sorted_dict.items():
        print(f'{code}: {num}')


for line in sys.stdin:
    """Loops through stdinput until CTRL-C is pressed"""
    n: int = 10
    my_lst: list = line.split(" ")
    status_code: str = my_lst[-2]
    if status_codes.get(status_code):
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1
    file_size: int = int(my_lst[-1])
    total_size += file_size
    count += 1
    if count == 10:
        print_logs(status_codes, total_size)
        count = 0

signal.signal(signal.SIGINT)
