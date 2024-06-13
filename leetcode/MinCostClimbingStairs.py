from decorators.Decorators import leetcode_test
from typing import List

@leetcode_test
def minCostClimbingStairs(cost: List[int]) -> int:
    cost.append(0)

    for i in range(len(cost)-3, -1, -1):
        cost[i] += min(cost[i+1],cost[i+2])

    return min(cost[0],cost[1])




cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]
cost3 = [0,1,2,2]

minCostClimbingStairs(cost1)
minCostClimbingStairs(cost2)
minCostClimbingStairs(cost3)