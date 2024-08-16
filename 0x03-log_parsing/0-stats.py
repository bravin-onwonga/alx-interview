#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""

import sys
import signal

if __name__ == '__main__':
    total_size = 0
    count = 0
    status_codes = {}

    def print_logs(status_codes: dict, total_size: int) -> None:
        """Handles printing after 10 lines are read and/or after
        CTRL-C is pressed with status codes sorted in ascending order
        Params:
            status_codes: a dict containing status codes and their occurence
            total_size: total file size at the time of printing
        Returns nothing
        """
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
            status_codes = {}

    signal.signal(signal.SIGINT)
