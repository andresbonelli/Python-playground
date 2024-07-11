from decorators.Decorators import leetcode_test
from typing import List


@leetcode_test
def product_except_self(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    pre, post = 1, 1

    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= post
        post *= nums[i]

    return result


nums = [1, 2, 3, 4]

product_except_self(nums)
