from decorators.Decorators import leetcode_test
from typing import List

"""
Given an integer array hours representing times in hours,
return an integer denoting the number of pairs i, j
where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.
"""

@leetcode_test
def countCompleteDayPairs(hours: List[int]) -> int:
    if len(hours) <= 1:
        return 0
    if len(hours) == 2:
        return 1 if sum(hours) % 24 == 0 else 0
    from collections import defaultdict
    hash_map = defaultdict(int)
    pairs = 0
    for hour in hours:
        if hour % 24 == 0:
            pairs += hash_map[0]
        else:
            pairs += hash_map[24 - hour % 24]
        hash_map[hour % 24] += 1
    return pairs


hours1 = [12, 12, 30, 24, 24]  # Output: 2
hours2 = [72, 48, 24, 3]  # Output: 3
countCompleteDayPairs(hours1)
countCompleteDayPairs(hours2)
