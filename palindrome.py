def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse

T = int(input())
for _ in range(T):
    num = int(input())
    if is_palindrome(num):
        print(f"{num} is a Palindrome Number.")
    else:
        print(f"{num} is NOT a Palindrome Number.")
