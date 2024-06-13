from decorators.Decorators import leetcode_test
"""
Given a string s, return true if it is a palindrome, or false otherwise.

"""

@leetcode_test
def isPalindrome(s: str) -> bool:
    left_pointer = l = 0
    right_pointer = r = len(s)-1
    while l <= r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


s = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
isPalindrome(s)
isPalindrome(s2)
isPalindrome(s3)




