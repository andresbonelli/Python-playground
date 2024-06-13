from decorators.Decorators import leetcode_test
"""
Given a string s, find the length of the longest substring without repeating characters.
"""
@leetcode_test
def lengthOfLongestSubstring(s: str) -> int:
    if not s or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    hash_set = set()
    left_pointer = l = 0
    right_pointer = r = 0
    answer = 0
    while r < len(s):
        char = s[r]
        while char in hash_set:
            hash_set.remove(s[l])
            l+=1
        hash_set.add(char)
        answer = max(answer, r-l+1)
        r+=1
    return answer




s = "abcabcbb"
lengthOfLongestSubstring(s)