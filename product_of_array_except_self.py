arr = list(map(int, input().strip("[]").split(",")))
n = len(arr)
result = []

for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= arr[j]

    result.append(product)

print(result)
