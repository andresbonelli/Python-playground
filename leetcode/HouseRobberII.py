from decorators.Decorators import leetcode_test
from typing import List
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""
@leetcode_test
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    if n <= 3:
        return max(nums)

    max_1, max_2 = nums[0], 0

    a, b = 0, 0
    for i in range(n-1):
        max_1 = max(a + nums[i], b)
        a = b
        b = max_1

    a, b = 0, 0
    for i in range(1,n):
        max_2 = max(a + nums[i], b)
        a = b
        b = max_2

    return max(max_1,max_2)


nums1 = [2,3,2]
nums2 = [1,2,3,1]
nums3 = [1,2,3]

rob(nums1)
rob(nums2)
rob(nums3)
