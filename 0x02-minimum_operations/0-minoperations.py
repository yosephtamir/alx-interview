#!/usr/bin/python3

"""
    used to calculate minimum operation
"""


def minOperations(n):
    """
    used to calculate minimum operation
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter