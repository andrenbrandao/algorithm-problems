"""
2269. Find the K-Beauty of a Number
https://leetcode.com/problems/find-the-k-beauty-of-a-number/
"""

"""
- Convert number to string
- Read the string in windows of size k
- Convert the substrings to integer
- If it is zero or cannot divide number, do not count
- Else, count as a k-beauty
- Return count

Reading and iterating over string: O(n)
Converting substring to integer: O(k)

Time Complexity: O(n*k)

Since k is << n. The time complexity is closer to O(n).
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        n = len(num_str)

        count = 0
        for i in range(n - k + 1):
            sub_num = int(num_str[i : i + k])
            if sub_num == 0 or num % sub_num != 0:
                continue

            count += 1

        return count
