def sumArray(arr):
    sum = 0
    for i in arr:
        sum +=i
    return sum
    
n = int(input())
arr = list(map(int, input().split()))
print(sumArray(arr))
