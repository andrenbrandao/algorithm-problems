"""
LeetCode 283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroPos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(i, zeroPos, nums)
                zeroPos += 1

    def swap(self, pos1, pos2, nums):
        nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
