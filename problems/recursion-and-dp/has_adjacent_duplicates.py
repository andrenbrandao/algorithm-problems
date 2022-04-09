"""
Given a string s, create a recursive boolean function that checks if it has
adjacent duplicates (the same character appearing in two successive indexes)

Example 1:
input: str = "programming"
output: true

Example 2:
input: str = "ababa"
output: false
"""


"""
Base cases:
empty string: false
one character: false
two characters: compare the two characters and return true or false

Recursive step:
- Compare the first two characters
- Call the recursive function with s[1:] characters

i
p

i
programming
"""


def hasAdjacentDuplicates(s):
    def helper(s, i):
        if i == len(s) or i == len(s) - 1:
            return False

        if s[i] == s[i + 1]:
            return True

        else:
            return False or helper(s, i + 1)

    return helper(s, 0)
