from decorators.Decorators import leetcode_test
from typing import List
"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence.
"""

@leetcode_test
def lengthOfLIS(nums: List[int]) -> int:
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],1+dp[j])

    return max(dp)

@leetcode_test
def lengthOfLIS_II(nums: List[int]) -> int:
    sub = []
    sub.append(nums[0])

    for num in nums:
        if num > sub[len(sub) - 1]:
            sub.append(num)
        else:
            j = binarySearch(sub, num)
            sub[j] = num

    return len(sub)

def binarySearch(sub: List[int], num: int) -> int:
    left_pointer = l = 0
    right_pointer = r = len(sub) - 1

    while l < r:
        mid_pointer = m = (l+r)//2
        if sub[m] == num:
            return m
        elif sub[m] < num:
            l = m+1
        else:
            r = m
    return l


nums1 = [10,9,2,5,3,7,101,18]
nums2 = [0,1,0,3,2,3]
nums3 = [7,7,7,7,7,7,7]

lengthOfLIS(nums1)
lengthOfLIS_II(nums1)
lengthOfLIS(nums2)
lengthOfLIS_II(nums2)
lengthOfLIS(nums3)
lengthOfLIS_II(nums3)
