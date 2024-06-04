"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[-1]


amount1, coins1 = 5, [1,2,5]
amount2, coins2 = 3, [2]
amount3, coins3 = 10, [10]
solution = Solution()
print(solution.change(amount1,coins1))
print(solution.change(amount2,coins2))
print(solution.change(amount3,coins3))
