"""
LeetCode 38. Count and Say
https://leetcode.com/problems/count-and-say/
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n - 1)

        new_say = []
        last_letter = say[0]
        count = 1
        for c in say[1:]:
            if last_letter == c:
                count += 1
            else:
                new_say.append(f"{count}{last_letter}")
                count = 1
            last_letter = c

        new_say.append(f"{count}{last_letter}")

        return "".join(new_say)
