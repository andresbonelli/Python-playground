from decorators.Decorators import leetcode_test

"""
An Armstrong (or 'Narcissistic') number is a number that is equal to
the sum of its own digits each raised to the power of the number of digits.
"""

@leetcode_test
def isArmstrong(num: int) -> bool:
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** len(str(num))
        temp //= 10

    return num == total


num1 = 407  # True. (4**3 + 0**3 + 7**3 == 407)
num2 = 663
num3 = 9474  # True. (9**4 + 4**4 + 7**4 + 4**4 == 9474)

isArmstrong(num1)
isArmstrong(num2)
isArmstrong(num3)