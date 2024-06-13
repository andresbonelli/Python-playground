from decorators.Decorators import leetcode_test

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

@leetcode_test
def isSubsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    p1, p2 = 0, 0

    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1

    return p1 == len(s)


s1, t1, = "abc", "ahbgdc"
s2, t2, = "axc", "ahbgdc"

isSubsequence(s1, t1)
isSubsequence(s2, t2)
