def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

def calculate_mode(numbers):
    freq = {}
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = max(freq.values())
    modes = []
    for key, val in freq.items():
        if val == max_freq:
            modes.append(key)

    if len(modes) == 1:
        return modes[0]
    else:
        return modes

nums = list(map(int, input().split()))

mean_val = calculate_mean(nums)
median_val = calculate_median(nums)
mode_val = calculate_mode(nums)

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)
