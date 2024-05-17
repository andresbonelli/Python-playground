"""
Given two different strings, find the lenght of the longest common substring between the two

"""


class Solution:
    def find_longest_common_substring(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        """for row in dp:
            print(row)"""
        return max_length

    def find_longest_common_substring_II(self, s1: str, s2: str) -> int:
        def check(length: int) -> bool:
            """ Check if there's a common substring of the given length. """
            if length == 0:
                return True
            hash_set = set()
            # Hash for s1
            for i in range(len(s1) - length + 1):
                substring = s1[i:i + length]
                hash_set.add(hash(substring))
            # Check against s2
            for i in range(len(s2) - length + 1):
                substring = s2[i:i + length]
                if hash(substring) in hash_set:
                    return True
            return False

        low, high = 0, min(len(s1), len(s2))
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
s2 = "She has this book I like to watch."
solution = Solution()
print(solution.find_longest_common_substring_II(s1, s2))
