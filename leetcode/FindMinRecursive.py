from decorators.Decorators import leetcode_test
from typing import List

@leetcode_test
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Base case: If the array contains only one element or already sorted
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]
    # Cheesy case if the array contains only two elements...
    if len(nums) == 2:
        return min(nums[0], nums[1])

    mid_pointer = m = len(nums) // 2
    if nums[m] < nums[m + 1] and nums[m] < nums[m - 1]:
        return nums[m]
    if nums[0] < nums[m]:
        return findMin(nums[m+1:])
    elif nums[0] > nums[m]:
        return findMin(nums[:m])

nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]

findMin(nums1)
findMin(nums2)
findMin(nums3)