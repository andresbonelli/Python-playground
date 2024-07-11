from decorators.Decorators import leetcode_test
from typing import List

"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
"""
@leetcode_test
def maxProduct(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    min_prod = nums[0]
    max_prod = nums[0]
    result = max_prod

    for i in range(1, len(nums)):
        temp_max_prod = max(nums[i], min_prod * nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i], max_prod * nums[i])
        max_prod = max(nums[i], temp_max_prod)
        result = max(result, max_prod)
    return result


nums1 = [2, 3, -2, 4]  # Output: 6
nums2 = [-2, 0, -1]  # Output: 0
maxProduct(nums1)
maxProduct(nums2)
