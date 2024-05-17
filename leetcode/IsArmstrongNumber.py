"""
An Armstrong (or 'Narcissistic') number is a number that is equal to
the sum of its own digits each raised to the power of the number of digits.
"""

class Solution(object):
    def isArmstrong(self, num: int) -> bool:
        total = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            total += digit ** len(str(num))
            temp //= 10

        return num == total


num1 = 407
num2 = 663
num3 = 9474
solution = Solution()
print(solution.isArmstrong(num1))
print(solution.isArmstrong(num2))
print(solution.isArmstrong(num3))