#!/usr/bin/python3
"""Parsing data into a particular format"""

import sys
import signal
total_size = 0
count = 0
status_codes = {}


def print_logs(status_codes, total_size):
    print(f'File size: {total_size}')
    for code, num in status_codes.items():
        print(f'{code}: {num}')


for line in sys.stdin:
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
