def uniqueOccurrences(arr):
    count = {}

    for i in arr:
        if i in count:
            count[i] += 1

        else:
            count[i] = 1

    freq_values = count.values()
    return len(freq_values) == len(set(freq_values))
        
T = int(input())
for i in range(T):
    arr = list(map(int, input().strip("[]").split(",")))
    result = uniqueOccurrences(arr)
    print(result)
