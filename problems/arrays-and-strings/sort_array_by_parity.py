"""
LeetCode 905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
"""

"""
-- SOLUTION --

   i j
[2,1,3,5]

- Use two pointers
- If left pointer is even, increment it
- Else
  - if right pointer is even, swap left and right
  - if right pointer is odd, decrement it
  - decrement right pointer
- Repeat while left < right

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            else:
                if nums[right] % 2 == 0:
                    nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return nums
