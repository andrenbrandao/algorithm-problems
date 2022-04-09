"""
LeetCode 47: Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all
possible unique permutations in any order.

"""

"""
## SOLUTION ##


          []
  /                 |         \
 [1]               [2]         [3]   n
/    \               /   \
[1,2] [1,3]        [2,1] [2,3]      n*(n-1)
/                   /       \
[1,2,3]  [1,3,2]   [2,1,3] [2,3,1]   n*(n-1)*(n-2)

 i
[1,2,3]

Base case:
- All elements have been used. len(permutation) == len(arr), then add this permutation to the result.
- Element is already used: return

Recursive step:
- We can take any of the elements for the first position
- Mark this element as visited
- Try to find another element that we can add to our array
- We can choose to add an element or not
- Repeat this process until all elements have been added

How can we prevent duplicates?
We can use a Set for the result.

How can we mark a element as used?
We can change its value to something like '#'and then return it back once we backtrack.

Time Complexity: O(n*n!)

T(0) = n
T(n) = n*T(n-1) + 1
     = n*((n-1)*T(n-2) + 1) + 1
     = n*(n-1)*T(n-2) + n + 1
     = n*(n-1)*( (n-2) * T(n-3) + 1 ) + n + 1
     = n*(n-1)*(n-2)*T(n-3) + n*(n-1) + n + 1
     = n!*n + n! + (n-1)! + .. n + 1
     = O(n*n!)

"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def rec(nums, permutation):
            if len(permutation) == len(nums):
                result.add(tuple(permutation))  # O(n)
                return

            for i in range(len(nums)):  # O(n)
                # has not been visited
                if nums[i] != "#":
                    tmp = nums[i]
                    nums[i] = "#"

                    permutation.append(tmp)
                    rec(nums, permutation)  # T(n-1)
                    permutation.pop()

                    nums[i] = tmp

        rec(nums, [])
        return list(map(list, result))  # O(n)
