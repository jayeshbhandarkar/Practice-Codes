# Sort an array according to the order defined by another array

from collections import Counter

def relative_sort(arr1, arr2):
    count = Counter(arr1)
    result = []

    for num in arr2:
        result.extend([num] * count[num])
        count.pop(num)

    remaining = sorted(count.elements())
    result.extend(remaining)

    return result

arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
arr2 = [2, 1, 8, 3]
result = relative_sort(arr1, arr2)
print(result)


"""def sample(arr1, arr2):
    count = {}
    for num in arr1:
        if num in count:
            count[num] += 1
        
        else:
            count[num] = 1

    result = []
    for num in arr2:
        if num in count:
            result.extend([num] * count[num])
            count.pop(num)

    remaining = []
    for num in count:
        remaining.extend([num] * count[num])

    result.extend(sorted(remaining))
    return result

arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
arr2 = [2, 1, 8, 3]
print(sample(arr1, arr2))"""
