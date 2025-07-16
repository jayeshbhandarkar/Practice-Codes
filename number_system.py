def sample(n, m):
    sum = 0
    for i in range(n, m+1):
        sum += (i**3)
    return sum
print(sample(2, 4))
