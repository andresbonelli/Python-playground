from decorators.Decorators import leetcode_test

"""
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""
@leetcode_test
def longestCommonSubsequence(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]


s1, t1 = "abcde", "ace"
s2, t2 = "abc", "abc"
s3, t3 = "abc", "def"
s4, t4 = "abcba", "abcbcba"

longestCommonSubsequence(s1,t1)
longestCommonSubsequence(s2,t2)
longestCommonSubsequence(s3,t3)
longestCommonSubsequence(s4,t4)
