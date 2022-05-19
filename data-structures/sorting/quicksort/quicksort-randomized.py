from random import randint

"""
For an array of size 10^6 the execution time of the randomized version was 10x faster.
I used an already sorted array, which is an example of a worst case scenario.
The algorithm by selection always the smallest element as the pivot makes n recursive calls
and because the partition step is O(n), it takes O(n^2) to execute.

Avg Quicksort: 47.597230195999146
Avg Quicksort Randomized: 4.145071268081665
"""


def quicksort_randomized(arr):
    def swap(arr, j, i):
        arr[i], arr[j] = arr[j], arr[i]

    def partition(arr, left, right):
        pivot = left

        j = left
        for i in range(left + 1, right + 1):
            if arr[i] <= arr[pivot]:
                j += 1
                swap(arr, j, i)

        new_pivot_pos = j
        swap(arr, pivot, new_pivot_pos)
        return new_pivot_pos

    def random_partition(arr, left, right):
        pivot = randint(left, right)
        swap(arr, left, pivot)
        return partition(arr, left, right)

    def sort(arr, left, right):
        if left < right:
            m = random_partition(arr, left, right)
            sort(arr, left, m - 1)
            sort(arr, m + 1, right)

    sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    quicksort_randomized(arr)
    print(arr)
