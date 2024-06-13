from decorators.Decorators import leetcode_test
from typing import List
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

@leetcode_test
def max_profit(prices: List[float]) -> float:
    min_price = dip = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] < dip:
            dip = prices[i]

        profit = max(profit, (prices[i] - dip))
    return profit


prices = [1,4,3,8,4,6,4,9,7,10,5,7,1,3,2,8,5]
max_profit(prices)

