"""
Given a positive integer n, create a recursive function that returns the sum of its digits.

Example 1:
input: n = 425
output: 11

Example 2:
input: n = 8009
output: 17
"""

"""
Base case:
n == 0: return 0

Recursive step:
- Take the last digit
- Sum it with the recursive function with the same number minus the last digit

P(n) = digit(n) + P(n-1)
"""


def sumOfDigits(n):
    if n == 0:
        return 0
    digit = n % 10
    remaining_number = n // 10
    return digit + sumOfDigits(remaining_number)
