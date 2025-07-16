def sample(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1

        else:
            count[i] = 1

    result = []

    for i in count:
        if count[i] % 2 == 0:
            result.append(i)

    return result

T = int(input())
for _ in range(T):
    arr = list(map(int, input().strip("[]").split(",")))
    result = sample(arr)
    print(*result)