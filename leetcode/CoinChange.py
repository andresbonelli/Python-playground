"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


coins1, amount1 = [1,2,5], 11
coins2, amount2 = [1]*1000, 4000
#coins3, amount3 = [1], 0
solution = Solution()
print(solution.coinChange(coins1,amount1))
print(solution.coinChange(coins2,amount2))
#print(solution.coinChange(coins3,amount3))
