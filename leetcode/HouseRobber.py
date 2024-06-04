"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses
have security systems connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        a, b = 0, 0
        max_amount = 0
        for i in range(n):
            max_amount = max(a + nums[i], b)
            a = b
            b = max_amount
        return max_amount


nums = [1,2,3,1]
nums2 = [2,7,9,3,1]
solution = Solution()
print(solution.rob(nums))
print(solution.rob(nums2))
