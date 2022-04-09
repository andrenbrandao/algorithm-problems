"""
Given a string s, create a recursive function that returns it reversed
"""

"""
Base cases:
a -> a
"" -> ""

Get the first element and add it to the end of the
recursive call.

P(s) = P(s[1:]) + s[0]

Wd also can go until the end and add them to a new list.

"""


def reverse(s):
    result = []

    def helper(s, i):
        if i == len(s):
            return

        helper(s, i + 1)
        result.append(s[i])

    helper(s, 0)
    return "".join(result)
