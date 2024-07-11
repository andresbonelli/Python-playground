from decorators.Decorators import leetcode_test
from typing import List
import random


@leetcode_test
def binary_search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left_pointer = l = 0
    right_pointer = r = len(nums) - 1

    while l <= r:
        mid_pointer = m = (l + r) // 2
        if nums[m] == target:
            return m
        elif target < nums[m]:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
    return -1


@leetcode_test
def recursive_binary_search(nums: List[int], target: int, offset=0) -> int:
    if len(nums) == 0:
        return -1

    left_pointer = l = 0
    right_pointer = r = len(nums) - 1
    mid_pointer = m = (l + r) // 2
    if nums[m] == target:
        return m + offset
    elif target < nums[m]:
        return recursive_binary_search(nums[:m], target, offset)
    elif nums[m] < target:
        return recursive_binary_search(nums[m + 1:], target, offset + m + 1)
    return -1


nums = [random.randint(0, 100) for _ in range(100)]

nums = list(set(sorted(nums)))

binary_search(nums, 50)
#recursive_binary_search(nums, 50)
