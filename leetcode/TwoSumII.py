"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int] | None:
        if len(numbers) <= 1:
            return None

        left_pointer = l = 0
        right_pointer = r = len(numbers)-1

        while l < r:
            if numbers[l]+numbers[r] == target:
                return [l, r]
            elif numbers[l]+numbers[r] > target:
                r -= 1
            else:
                l += 1
        return None


numbers = [2, 7, 11, 15]
target = 9
numbers2 = [-1,0]
target2 = -1
solution = Solution()
numbers3 = [2,3,4]
target3 = 6
print(solution.twoSum(numbers,target))
print(solution.twoSum(numbers2,target2))
print(solution.twoSum(numbers3,target3))