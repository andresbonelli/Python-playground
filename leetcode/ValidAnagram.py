"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
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
s3, t3 = "nigger", "ginger"
s4, t4 = "aacc", "ccac"
solution = Solution()
print(solution.isAnagram(s1,t1))
print(solution.isAnagram(s2,t2))
print(solution.isAnagram(s3,t3))
print(solution.isAnagram(s4,t4))