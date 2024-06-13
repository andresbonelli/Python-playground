from decorators.Decorators import leetcode_test
from typing import List
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""


@leetcode_test
def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i][:len(prefix)] != prefix:
            prefix = prefix[:len(prefix)-1]
            if not prefix:
                return ""

    return prefix

@leetcode_test
def longestCommonPrefixII(strs: List[str]) -> str:
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

longestCommonPrefix(strs)
longestCommonPrefixII(strs)
longestCommonPrefix(strs2)
longestCommonPrefixII(strs2)
longestCommonPrefix(strs3)
longestCommonPrefixII(strs3)
