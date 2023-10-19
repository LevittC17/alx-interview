#!/usr/bin/python3

'''
:param total_size: Total file size accumulated so far.
:param status_codes: Dictionary containing counts for
each status code.
'''


import sys


def print_stats(total_size, status_codes):
    """
    Print statistics including total file size and status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """
    Main function for processing log lines and computing statistics.
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if status_code in status_codes:
                status_codes[status_code] += 1
                total_size += file_size

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    # Print the final statistics
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
