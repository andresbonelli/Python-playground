"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(n-2):
            total = a + b
            a = b
            b = total
        return b



n = 3
solution = Solution()
print(solution.climbStairs(n))

