"""
Given an integer n, create a function that returns as strings all the n-bits
boolean numbers that have at most 2 zeros.

Example:
input: n = 4
output: ['0011', '0101', '0110', '0111', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
"""


"""
      ''
     /   \
     0    1
    / \    / \
   00  01 10  11
  /  \
 000 001
  |
  X


Base case:
- n_zeros == 3: return
- n == 0: append current_bits to result; return;

Recursive step:
- Start from empty string
- We can add a 0 or add a 1
- Repeat until we have more zeroes than we can have or we do not have any more bits to add

Time Complexity: O(n*2^n)
Space Complexity: O(n*2^n)
"""


def binaryNumbers(n):
    result = []

    def recHelper(n, current_bits, n_zeros):
        if n_zeros == 3:
            return

        if n == 0:
            result.append(current_bits)
            return

        recHelper(n - 1, current_bits + "0", n_zeros + 1)
        recHelper(n - 1, current_bits + "1", n_zeros)

    recHelper(n, "", 0)
    return result
