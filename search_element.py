def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

T = int(input())
for _ in range(T):
    arr = list(map(int, input().strip("[]").split(",")))
    target = int(input())
    index = search(arr, target)
    
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")
