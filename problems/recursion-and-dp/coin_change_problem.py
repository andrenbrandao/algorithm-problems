
"""
HackerRank - The Coin Change Problem
https://www.hackerrank.com/challenges/coin-change/problem
"""


#!/bin/python3

"""
n = 3
coins = [8,1,2,3]

[1,1,1]
[1,2]
[3]


           3
        /  | \  \
    -5 (X) 2  1  0
           | \
           1  0
           |
           0

We can start with the amount 3 and try to use
each of the coins recursively.
If we reach zero, we have found one way to solve it.
We return 1 from the leaf nodes and sum them in the end.

- Start from the amount n
- For each coin, try to take that amount
(we do not go back to coins we have already used, otherwise we would make different
combinations)
- If we reach zero, return 1, if less than zero, return 0

Time Complexity: O(coins ^ amount)
Space Complexity: O(amount)

However, we can use memoization/dynamic programming to speed this up.

- For every amount we have found, we memoize the nways to find a solution
on that amount.

Time Complexity: O(coins * amount)
Space Complexity: O(amount)



"""

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(amount, coins):
    memo = dict()

    def getWaysRec(amount, coins, pos):
        if amount < 0:
            return 0

        if amount == 0:
            return 1

        if (amount, pos) in memo:
            return memo[(amount, pos)]

        n_ways = 0
        for coin_pos in range(pos, len(coins)):
            n_ways += getWaysRec(amount-coins[coin_pos], coins, coin_pos)

        memo[(amount, pos)] = n_ways
        return n_ways

    return getWaysRec(amount, coins, 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
