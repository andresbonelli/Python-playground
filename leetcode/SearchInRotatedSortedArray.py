def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left_pointer = l = 0
    right_pointer = r = len(nums) - 1

    while l <= r:

        mid_pointer = m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target >= nums[l] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1
    return -1


nums = [5, 1, 3]
target = 0

print(search(nums, target))
