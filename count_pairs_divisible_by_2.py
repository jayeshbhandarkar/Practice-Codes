def sample(arr):
    odd_count = 0
    even_count = 0
    
    for i in arr:
        if i % 2 == 0:
            even_count += 1
            
        else:
            odd_count += 1
            
    even = (even_count * (even_count - 1)) // 2
    odd = (odd_count * (odd_count - 1)) // 2
            
    return even + odd
    
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = sample(arr)
    print(result)
    