def quicksort(arr):
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

    def sort(arr, left, right):
        if left < right:
            m = partition(arr, left, right)
            sort(arr, left, m - 1)
            sort(arr, m + 1, right)

    sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    quicksort(arr)
    print(arr)
