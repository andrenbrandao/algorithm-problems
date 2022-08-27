"""
LeetCode 162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
"""

"""
We can iterate over the array and look at the left and right neighbors.
If the element is greater than both, we have a peak.

Time Complexity: O(n)

But, we need to find a log(n) algorithm.

---

Since we need to find a logn algorithm, we have to use binary search.
But, how if the array is not sorted?

[1,2,1,3,5,6,4]

We can check the middle element and its neighbors. If it is growing to the left side,
we divide the array by 2 and look now on the left side. Otherwise, look to the right.
Or, the element is already a peak, so return it.

TC: O(logn)
SC: O(1)

"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            leftNeighbor = float('-inf') if mid - 1 < 0 else nums[mid-1]
            rightNeighbor = float('-inf') if mid + 1 == len(nums) else nums[mid+1]
            currentVal = nums[mid]

            if currentVal > leftNeighbor and currentVal > rightNeighbor:
                return mid
            elif currentVal > leftNeighbor:
                left = mid + 1
            else:
                right = mid - 1

        return -1
