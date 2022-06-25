"""
LeetCode 2279. Maximum Bags With Full Capacity of Rocks
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
"""


"""
capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2

[2,3,4,5]
[1,2,4,4]
[1,1,0,1] = diff

capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100

[10,2,2]
[2, 2,0]
[8,0,2]

We want to fill the ones with the least diff first. Keep doing this until
we have used all the additional rocks or have filled all bags.

- Create diff array
- Sort it
- From the smallest, try to take the maximum amount we can of additional rocks
- Repeat until we cannot take any more or have passed through all bags
- Return count of zero in diff

TC: O(nlogn)
SC: O(n)

"""
from typing import List


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        n = len(capacity)
        diff = [0] * n
        for i in range(n):
            diff[i] = capacity[i] - rocks[i]

        sorted_diff = sorted(diff)

        for i in range(n):
            if sorted_diff[i] > additionalRocks:
                break

            additionalRocks -= sorted_diff[i]
            sorted_diff[i] = 0

        return sorted_diff.count(0)
