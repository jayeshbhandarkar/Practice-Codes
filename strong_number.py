def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def is_strong_number(n):
    original = n
    sum_of_factorials = 0

    while n > 0:
        digit = n % 10
        sum_of_factorials += factorial(digit)
        n //= 10

    return sum_of_factorials == original

n = int(input("Enter a number: "))
if is_strong_number(n):
    print("Yes")
else:
    print("No")
