#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""
import sys


def print_stats(size, status_codes):
    """
    Prints the accumulated statistics.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                # The file size is the last element
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                # The status code is the second to last element
                if line[-2] in status_codes.keys():  # Check string first
                    status_codes[line[-2]] += 1
                else:
                    # Try converting to int to check against keys
                    code = int(line[-2])
                    if code in status_codes:
                        status_codes[code] += 1
            except (IndexError, ValueError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
