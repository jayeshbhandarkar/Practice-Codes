# Solution : Brute Force Approach (O(n))

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # return factors
    return ",".join(map(str, factors))  # Convert list to comma-separated string

t = int(input())
for _ in range(t):
    n = int(input())
    result = find_factors(n)
    print(*result)


# Solution : Optimized Approach Using Square Root (O(√n))

"""
def find_factors_efficient(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):  
        if n % i == 0:
            factors.add(i)        
            factors.add(n // i)    

    #return sorted(factors) 
    return ",".join(map(str, sorted(factors)))  # Convert list to comma-separated string

n = int(input("Enter a number: "))
print("Factors:", find_factors_efficient(n))
"""
