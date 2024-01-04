#!/usr/bin/python3
"""Pascal"""


def pascal_triangle(n):
    """fucnrion to get the number of pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for x in range(n):
        new_row = [0] * (x+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, x):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[x - 1][j]
                b = pascal_triangle[x - 1][j - 1]
                new_row[j] = a + b

        pascal_triangle[x] = new_row

    return pascal_triangle
