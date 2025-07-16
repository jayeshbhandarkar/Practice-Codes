def rearrangeArray(arr):
    arr.sort()  # Sort the array in ascending order
    n = len(arr)
    first_half = arr[:n//2]  # First half in increasing order
    second_half = arr[n//2:]  # Second half in decreasing order
    second_half.reverse()  # Reverse the second half

    return first_half + second_half  # Concatenate both halves

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(*rearrangeArray(arr1))  
print(*rearrangeArray(arr2))
