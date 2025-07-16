def maximum_frequency(nums):
    count = {}

    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    max_freq = max(count.values())
    total = 0

    for freq in count.values():
        if freq == max_freq:
            total += freq

    return total

nums = list(map(int, input().strip("[]").split(",")))
print(maximum_frequency(nums))
