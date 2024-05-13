def findMin(nums):
    if len(nums) == 1:
        return nums[0]

    left_pointer = l = 0
    right_pointer = r = len(nums) - 1
    answer = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            answer = min(answer, nums[l])
        mid_pointer = m = (l + r) // 2
        answer = min(answer, nums[m])
        if nums[l] <= nums[m]:
            l = m + 1
        else:
            r = m - 1
    return answer

nums1 = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]

print(findMin(nums1))
print(findMin(nums2))
print(findMin(nums3))