"""
LeetCode 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestLength = min([len(text) for text in strs])
        commonPrefix = []
        matches = True

        for i in range(smallestLength):
            letter = strs[0][i]

            for text in strs:
                if text[i] != letter:
                    matches = False
                    break

            if not matches:
                break

            commonPrefix.append(letter)

        return "".join(commonPrefix)
