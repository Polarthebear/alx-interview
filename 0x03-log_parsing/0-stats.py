#!/usr/bin/python3
"""
Module that reads stdin line by line
and computes it's metrics
"""

import sys


def print_stats(stats: dict, filesize: int) -> None:
    """Print the stats of the file size and status codes"""
    print("File size: {:d}".format(filesize))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


filesize = 0
count = 0
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
stats = {k: 0 for k in codes}


try:
    for line in sys.stdin:
        count += 1
        data = line.split()

        try:
            status_code = data[-2]
            if status_code in stats:
                stats[status_code] += 1
        except Exception:
            pass

        try:
            filesize += int(data[-1])
        except Exception:
            pass

        if count % 10 == 0:
            print_stats(stats, filesize)

    print_stats(stats, filesize)

except KeyboardInterrupt:
    print_stats(stats, filesize)
    raise


if __name__ == '__main__':
    pass
