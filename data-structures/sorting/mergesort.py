import sys


def merge(a, b):
    c = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def mergesort(arr):
    length = len(arr)
    if length == 1:
        return arr

    a = mergesort(arr[: length // 2])
    b = mergesort(arr[length // 2 :])
    c = merge(a, b)

    return c


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    sorted_arr = mergesort(arr)
    print(sorted_arr)
