"""
Given a string S(input consisting) of '*' and '#'. The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of '*' and '#' in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0

Example 1:
Input 1:
###***   -> Value of S

Output :
0   → number of * and # are equal
"""

# Solution 1
"""
def min_to_make_valid(s):
    # Count the number of '*' and '#'
    star_count = s.count('*')
    hash_count = s.count('#')

    print(star_count - hash_count)

s = input("Enter string: ")
print(min_to_make_valid(s))
"""

# Solution 2
s=input("Enter String: ")
a=0
b=0
for i in s:
    if i=='*':
        a+=1
    elif i=='#':
        b+=1
print(a-b)