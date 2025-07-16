def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

arr = [7, 9, 6, 4, 11]
target = 9

result = linear(arr, target)
print(result)
