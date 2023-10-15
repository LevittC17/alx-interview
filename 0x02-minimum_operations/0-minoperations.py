#!/usr/bin/env python3

'''
Calculate the fewest number of opeerations needed
to obtain `n` H characters
'''


def minOperations(n):
    '''Return the minimum number of perations required to achieve
    `n` H characters. If `n` is impossible to achieve, return 0'''
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    return operations
