#!/usr/bin/python3
"""
Function that calculates fewest number
of operations needed to result some characters in the file.
"""


def minOperations(n):
    """Module for minOperations"""
    temp = 0
    dp = 1

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                temp += i
                dp *= i
                n = n // i
                break
    return temp
