def isPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return "Not Palindrome"
        else:
            left += 1
            right -= 1
    return "Palindrome"

T = int(input())
for _ in range(T):
    s = input()
    result = isPalindrome(s)
    print(result)
