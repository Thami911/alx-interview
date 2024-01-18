#!/usr/bin/python3
"""
    Method of determining the number of minmum operations given to characters n
"""

def minOperations(n):
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
