"""
Given a string s, create a function that returns all its possible subsequences, the order doesn't matter.

Example 1:
- Input: str = "abcd"
- Output:  ["abcd", "abc", "abd", "ab", "acd", "ac", "ad", "a", "bcd", "bc", "bd", "b", "cd", "c", "d", ""]



## SOLUTION ##


             ''
        /        \
       ''         a        2
   /     \        / \
  ''      b      a   ab    2^2
 / \    /  \    / \
''  c  b    bc  a ac ...   2^i
....

At every position we can include the character of the string or not.

Base case:
pos > len(str): append the current string and return

Recursive Step:
- Start from an empty string
- Add the next character to our string or not
- If are over the string limit, we append the currentString to our result

Time Complexity: O(2^n)
Space Complexity: O(n)

-- Time complexity is actually O(n*2^n)
-- Space complexity is also O(n*2^n)
because of the number of subsequences is 2^n and each
subsequence can have at most n characters

T(0) = n

T(n) = 2T(n-1) + 2
     = 2(2T(n-2) + 2 ) + 2
     = 4T(n-2) + 4 + 2
     = 4( 2T(n-3) + 2 ) + 4 + 2
     = 8T(n-3) + 8 + 4 + 2
     = 8 ( 2T(n-4) + 2 ) + 8 + 4 + 2
     = 16T(n-4) + 16 + 8 + 4 + 2
     = 2^k*T(n-k) + 2^k + 2^k-1 ... + 2
     = 2^n*T(n-n) + ...
     = 2^n*T(0)
     = (2^n)*n
"""


def getSubsequences(s):
    result = []

    def recursiveGetSubsequences(s, pos, current_string):
        if pos == len(s):
            result.append("".join(current_string))  # O(n)
            return

        # including the character
        current_string.append(s[pos])  # 1
        recursiveGetSubsequences(s, pos + 1, current_string)  # T(n-1)
        current_string.pop()  # 1

        # not including the character
        recursiveGetSubsequences(s, pos + 1, current_string)  # T(n-1)

    recursiveGetSubsequences(s, 0, [])
    return result
