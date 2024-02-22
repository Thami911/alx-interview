#!/usr/bin/python3
'''2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotates a 2d matrix 90° clockwise
    Returns: Nothing'''
    left, right = 0, len(matrix) - 1

    while left < right:
        for x in range(right - left):
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + x]
            # move bottom left to top left
            matrix[top][left + x] = matrix[bottom - x][left]
            # move bottom right to bottom left
            matrix[bottom - x][left] = matrix[bottom][right - x]
            # move top right to bottom right
            matrix[bottom][right - x] = matrix[top + x][right]
            # move top left to top right
            matrix[top + x][right] = topLeft
        right -= 1
        left += 1
