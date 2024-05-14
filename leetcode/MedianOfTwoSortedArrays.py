"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
class Solution(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # nums1 should always be the array with fewer elements.
        if len(nums1) > len(nums2):
            return self.find_median_sorted_arrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        start_pointer = s = 0
        end_pointer = e = x

        while s <= e:
            part_x = (s+e)//2
            part_y = (x+y+1)//2 - part_x

            x_left = float('-inf') if part_x == 0 else nums1[part_x-1]
            x_right = float('inf') if part_x == x else nums1[part_x]
            y_left = float('-inf') if part_y == 0 else nums2[part_y - 1]
            y_right = float('inf') if part_y == y else nums2[part_y]

            # optimal case: all elements in the left part of both nums1 and nums2 are smaller than
            # the right part, meaning both half are already sorted.
            if x_left <= y_right and y_left <= x_right:
                # case for EVEN total number of elements (median is between two elements)
                if (x+y) % 2 == 0:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2
                # case for ODD total number of elements (median is a single element)
                else:
                    return max(x_left, y_left)
            # shift END pointer <- if there is still a larger element in the left part of NUMS1
            elif x_left > y_right:
                e = part_x - 1
            # shift START pointer -> if there is still a larger element in the left part of NUMS2
            else:
                s = part_x + 1

        return 0


nums1 = [1, 3]
nums2 = [2, 7]
solution = Solution()
print(solution.find_median_sorted_arrays(nums1, nums2))