"""
Given an array of integers arr and integer num, create a recursive
function that returns the number of ocurrences of num in arr.

Example 1:
input: arr = [4,2,7,4,4,1,2], num = 4
output: 3
"""


def countOccurrences(arr, num):
    def recCount(arr, num, i):
        if i == len(arr):
            return 0

        count = 0
        if num == arr[i]:
            count += 1
        return count + recCount(arr, num, i + 1)

    return recCount(arr, num, 0)
