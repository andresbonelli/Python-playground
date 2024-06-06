"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:len(prefix)-1]
                if not prefix:
                    return ""

        return prefix

    def longestCommonPrefixII(self, strs: list[str]) -> str:
        prefix = ""
        for i, char in enumerate(strs[0]):
            for s in strs:
                if i < len(s):
                    if char != s[i]:
                        return prefix
                else:
                    return prefix
            prefix += char
        return strs[0]




strs = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = ["ab", "a"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
print(solution.longestCommonPrefix(strs2))
print(solution.longestCommonPrefix(strs3))
print(solution.longestCommonPrefixII(strs))
print(solution.longestCommonPrefixII(strs2))
print(solution.longestCommonPrefixII(strs3))
