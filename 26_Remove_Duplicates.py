# LeetCode 26 - Remove Duplicates from Sorted Array

# Problem Link:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Solution:

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j


# Example:
# Input: nums = [1, 1, 2, 2, 3]
# Output: 3
# Modified nums: [1, 2, 3, _, _]

# Time Complexity: O(n)
# Space Complexity: O(1)
