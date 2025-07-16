def is_harshad(n):
    sum_of_digits = 0
    temp = n

    while temp > 0:
        sum_of_digits += temp % 10  
        temp //= 10

    return n % sum_of_digits == 0

num = int(input("Enter a number: "))

if is_harshad(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is NOT a Harshad Number.")


"""
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def is_harshad(n):
    return n % sum_of_digits(n) == 0

num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is NOT a Harshad Number.")
"""
