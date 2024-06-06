"""
Given two different strings, find the lenght of the longest common substring between the two

"""


class Solution:
    def find_longest_common_substring(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # init 2D matrix n * m
        dp = [[0] * (n + 1)] * (m + 1)
        # init result
        max_length = 0
        # loop through dp matrix once, storing max contiguous characters up to each point.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length

    def find_longest_common_substring_II(self, s: str, t: str) -> int:
        def check(length: int) -> bool:
            # Check if there's a common substring of the given length.
            if length == 0:
                return True
            hash_set = set()
            # Hash for s
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                hash_set.add(hash(substring))
            # Check against t
            for i in range(len(t) - length + 1):
                substring = t[i:i + length]
                if hash(substring) in hash_set:
                    return True
            return False

        low, high = 0, min(len(s), len(t))
        result = 0

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result


s1 = "I have this book I like to read."
t1 = "She has this book I like to watch."
solution = Solution()
print(solution.find_longest_common_substring(s1, t1))
