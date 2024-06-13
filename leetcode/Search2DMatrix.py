from decorators.Decorators import leetcode_test
from typing import List
"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""


@leetcode_test
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    top_pointer = t = 0
    bottom_pointer = b = rows - 1
    left_pointer = l = 0
    right_pointer = r = cols - 1

    # STEP 1) Perform binary search to find which "row" contains target value.
    while t <= b:
        mid_pointer = m = (t + b) // 2
        if target > matrix[m][-1]:
            t = m + 1
        elif target < matrix[m][0]:
            b = m - 1
        else:
            break
    if not (t <= b):
        return False

    row = (t + b) // 2
    # STEP 2) Perform binary search within row to find target value.
    while l <= r:
        mid_pointer = m = (l + r) // 2
        if target == matrix[row][m]:
            return True
        elif target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
    return False


matrix1, target1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
matrix2, target2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13

searchMatrix(matrix1, target1)
searchMatrix(matrix2, target2)
