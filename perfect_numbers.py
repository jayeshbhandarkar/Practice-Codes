def is_perfect(n):
    if n <= 1:
        return False    
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    
    return total == n

T = int(input())
for _ in range(T):
    num = int(input("Enter a number: "))
    if is_perfect(num):
        print(f"{num} is a Perfect Number.")
    else:
        print(f"{num} is NOT a Perfect Number.")
