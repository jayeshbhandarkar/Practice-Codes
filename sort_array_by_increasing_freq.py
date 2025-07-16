# Sort Array by Increasing Frequency
# Input : [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
# Output : [5, 4, 12, 12, 2, 2, 2, 3, 3, 3, 3]

def frequencySort(nums):
    count = {}

    for i in nums:
        if i in count:
            count[i] += 1

        else:
            count[i] = 1

    result = sorted(nums, key=lambda x: (count[x], -x)) 
    # decreasing frequency
    # result = sorted(nums, key=lambda x: (-count[x], x))

    return result

nums = list(map(int, input().strip("[]").split(",")))
result = frequencySort(nums)
print(result)
