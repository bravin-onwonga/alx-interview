#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""

import sys

total_size = 0
count = 0
status_codes = {}
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]


if __name__ == '__main__':
    def print_logs(status_codes: dict, total_size: int) -> None:
        """Handles printing after 10 lines are read and/or after
        CTRL-C is pressed with status codes sorted in ascending order
        Params:
            status_codes: a dict containing status codes and their occurence
            total_size: total file size at the time of printing
        Returns nothing
        """
        print(f'File size: {total_size}')
        for code, num in sorted(status_codes.items()):
            print(f'{code}: {num}')
    try:
        for line in sys.stdin:
            """Loops through stdinput until CTRL-C is pressed
            Returns nothing
            """
            my_lst = line.split(" ")
            try:
                status_code = my_lst[-2]
                file_size = int(my_lst[-1])
                if status_code not in codes:
                    if file_size:
                        total_size += file_size
                    continue
                if status_codes.get(status_code):
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1
                total_size += file_size
                count += 1
                if count == 10:
                    print_logs(status_codes, total_size)
                    count = 0
            except BaseException:
                pass
        print_logs(status_codes, total_size)
    except KeyboardInterrupt:
        print_logs(status_codes, total_size)
        raise
