from decorators.Decorators import leetcode_test

"""
Given an integer x, return true if x is a
palindrome, and false otherwise.
"""

@leetcode_test
def isPalindrome(x: int) -> bool:
    num = str(x)
    left_pointer = l = 0
    right_pointer = r = len(num) - 1

    while l <= r:
        if num[l] == "-":
            return False
        if num[l] != num[r]:
            return False
        l += 1
        r -= 1
    return True


n1 = 121
n2 = -121
n3 = 1000021

isPalindrome(n1)
isPalindrome(n2)
isPalindrome(n3)
