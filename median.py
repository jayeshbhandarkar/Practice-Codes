def median(n, arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    
n = int(input())
arr = list(map(int, input().split()))
print(median(n, arr))
