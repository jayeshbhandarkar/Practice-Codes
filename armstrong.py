def armstrong(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + armstrong(n // 10, digits)

def is_armstrong(n):
    digits = len(str(n))
    return n == armstrong(n, digits)

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is NOT an Armstrong Number.")
