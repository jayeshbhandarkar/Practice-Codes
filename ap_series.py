def sum_of_ap(n, a, d):
    return (n * (2 * a + (n - 1) * d)) // 2
 
T = int(input())
for _ in range(T):
    n, a, d = map(int, input().split())
    print(sum_of_ap(n, a, d))

"""
def sum_of_ap(n, a, d):
    total = 0
    for i in range(n):
        total += a + i * d
    return total

T = int(input())
for _ in range(T):
    n, a, d = map(int, input().split())
    print(sum_of_ap(n, a, d))
"""
