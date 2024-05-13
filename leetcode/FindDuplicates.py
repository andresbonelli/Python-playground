class Solution(object):
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_set = set()
        for i in range(len(nums)):
            if nums[i] in hash_set:
                return True
            else:
                hash_set.add(nums[i])
        return False

    def contains_duplicate_II(self, nums, k):
        """Given an integer array nums and an integer k,
        return true if there are two distinct indices i and j in the array
        such that nums[i] == nums[j] and abs(i - j) <= k."""
        hash_set = set()
        for i in range(len(nums)):
            if nums[i] in hash_set:
                return True
            hash_set.add(nums[i])
            if len(hash_set) > k:
                hash_set.remove(nums[i - k])
        return False

nums = [4,1,2,3,1,5]
solution = Solution()
print(solution.contains_duplicate_II(nums=nums, k=3))