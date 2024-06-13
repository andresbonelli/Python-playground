from decorators.Decorators import leetcode_test

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

@leetcode_test
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for i in count:
        if i != 0:
            return False
    return True


s1, t1 = "anagram", "nagamar"
s2, t2 = "rat", "car"
s4, t4 = "aacc", "ccac"

isAnagram(s1,t1)
isAnagram(s2,t2)
isAnagram(s4,t4)