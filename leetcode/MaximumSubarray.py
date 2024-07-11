from decorators.Decorators import leetcode_test
from typing import List
"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
@leetcode_test
def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    cur = 0
    maxx = nums[0]
    for num in nums:
        if cur < 0:
            cur = 0
        cur += num
        maxx = max(maxx,cur)
    return maxx


nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [5,4,-1,7,8]
maxSubArray(nums1)
maxSubArray(nums2)
maxSubArray(nums3)