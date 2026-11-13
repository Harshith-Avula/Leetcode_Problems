# LeetCode 283 - Move Zeroes

# Problem Link:
# https://leetcode.com/problems/move-zeroes/

# Solution:

class Solution:
    def moveZeroes(self, nums):
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums


# Example:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# Time Complexity: O(n)
# Space Complexity: O(1)
