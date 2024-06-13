from decorators.Decorators import leetcode_test
from typing import List
"""
Given a string s, return the longest palindromic substring in s.
"""


@leetcode_test
def longestPalindrome(s: str) -> str:
    if len(s) < 1:
        return ""
    left_pointer = l = 0
    right_pointer = r = 0
    for i in range(len(s)):
        len_1 = checkPalinrome(s,i,i) # odd palindrome
        len_2 = checkPalinrome(s,i,i+1) # even palindrome
        total_len = max(len_1,len_2)
        if total_len > r - l:
            l = i - (total_len-1)//2
            r = i + total_len//2
    return s[l:r+1]

def checkPalinrome(s: str, left_pointer: int, right_pointer: int) -> int:
    l = left_pointer
    r = right_pointer
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r-l-1


s1 = "babad"
s2 = "bb"

longestPalindrome(s1)
longestPalindrome(s2)

