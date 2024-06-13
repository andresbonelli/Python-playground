from decorators.Decorators import leetcode_test
from typing import List

@leetcode_test
def maxSubArray(nums: List[int]) -> int:
    curSum = 0
    maxSum = nums[0]

    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSum = max(curSum, maxSum)

    return maxSum

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

nums = [0,1]
maxSubArray(nums)
maxProduct(nums)
