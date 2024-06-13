from decorators.Decorators import leetcode_test
from typing import List, Tuple
"""
 Search for the index of pair of numbers that sum up to a target value using the two-pointer approach.

:param array: (list[int]) A list of integers (later sorted in ascending order).
:param target: (int) The target sum to find.
:return: A tuple containing the indexes of the pair of numbers that sum up to the target value
         (or None if no such pair exists).
"""
@leetcode_test
def two_sum(array: List[int], target: int) -> Tuple[int, int] | None:
    sorted_arr = sorted(array)
    n = len(sorted_arr)
    left = 0
    right = n - 1

    while left < right:
        summ = sorted_arr[left] + sorted_arr[right]
        if summ == target:

            return array.index(sorted_arr[left]), array.index(sorted_arr[right])
        elif summ < target:
            left += 1
        elif summ > target:
            right -= 1
    return None

@leetcode_test
def two_sum_no_sort(array: List[int], target: int) -> Tuple[int, int] | None:
    n = len(array)
    hash_map = {}

    for i in range(n):
        diff = target - array[i]
        if diff in hash_map:
            return hash_map[diff], i
        else:
            hash_map[array[i]] = i

    return None


arr = [2, 7, 11, 15]
arr2 = [3, 2, 4]
arr3 = [3, 3]
two_sum_no_sort(arr, 9)
two_sum_no_sort(arr2, 6)
two_sum_no_sort(arr3, 6)
