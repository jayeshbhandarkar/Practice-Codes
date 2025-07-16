def rotate_array(nums, k):
    n = len(nums)

    k = k % n

    nums.reverse()

    nums[:k] = reversed(nums[:k])

    nums[k:] = reversed(nums[k:])

    return nums

print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_array([10, 20, 30, 40, 50], 2))
print(rotate_array([1, 2, 3, 4, 5], 7))
print(rotate_array([5, 10, 15, 20], 0))