from decorators.Decorators import leetcode_test
from typing import List
import random


@leetcode_test
def findSmallest(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    answer = nums[0]
    for num in nums:
        answer = min(num, answer)

    return answer


nums1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
findSmallest(nums1)
