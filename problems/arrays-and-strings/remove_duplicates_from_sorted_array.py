"""
LeetCode 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n

        i = 0
        j = 1
        while i < n and j < n:
            if nums[i] < nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                j += 1

        return i + 1
