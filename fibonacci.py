def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 10
print(f"Fibonacci of {n} is {fibonacci_recursive(n)}")

# ------------------------------------------------------------------------------

"""
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10
print(f"Fibonacci of {n} is {fibonacci_iterative(n)}")
"""

# ------------------------------------------------------------------------------

# Print Fibonacci Series up to Nth term -

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def print_fibonacci_series(n):
    for i in range(n+1):
        print(fibonacci_recursive(i), end=" ")  # Printing Fibonacci numbers

n = 10 
print_fibonacci_series(n)
