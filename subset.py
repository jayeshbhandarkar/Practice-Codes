def is_subset(arr1, arr2):
    arr = set(arr2)

    for i in arr1:
       if i not in arr:
              return "arr1[] is not a subset of arr2[]"
        
       return "arr1[] is a subset of arr2[]"

T = int(input())

for _ in range(T):
    arr1 = list(map(int, input().strip("[]").split(",")))
    arr2 = list(map(int, input().strip("[]").split(",")))
    result = is_subset(arr1, arr2)
    print(result)
