from decorators.Decorators import leetcode_test

"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-'
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1
and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
"""


@leetcode_test
def findTargetSumWays(nums: list[int], target: int) -> int:
    summ = sum(nums)
    if (target + summ) % 2 != 0 or summ < abs(target):
        return 0
    s1 = (target + summ) // 2
    if s1 < 0:
        return 0

    dp = [1] + [0] * s1

    for num in nums:
        for i in range(s1, num-1, -1):
            dp[i] = dp[i] + dp[i-num]

    return dp[s1]


nums1, target1 = [1, 1, 1, 1, 1], 3
nums2, target2 = [1], 1

findTargetSumWays(nums1, target1)
findTargetSumWays(nums2, target2)
