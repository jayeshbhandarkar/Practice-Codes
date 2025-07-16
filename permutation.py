# ---------------------------------------------------------------------------------------

import math
def permutations(N, R):
    return math.factorial(N) // math.factorial(N - R)

print(permutations(5, 3))  
print(permutations(6, 4)) 

# ---------------------------------------------------------------------------------------

"""
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def permutations(N, R):
    return factorial(N) // factorial(N - R)

N, R = map(int, input().split())
result = permutations(N, R)
print(result)
"""