def binary(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

arr = [7, 5, 4, 9, 11]
target = 9
result = binary(arr, target)
print(result)