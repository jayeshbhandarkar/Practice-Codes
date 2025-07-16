def leftRotateSimple(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

print(leftRotateSimple([1, 2, 3, 4, 5], 2))
print(leftRotateSimple([1, 2, 3, 4, 5, 6, 7], 3))
