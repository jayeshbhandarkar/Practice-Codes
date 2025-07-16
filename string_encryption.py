"""
Bingu was testing all the strings he had at his place and found that most of them were prone to a vicious attack by 
Banju, his arch-enemy. Bingu decided to encrypt all the strings he had, by the following method. Every substring of 
identical letters is replaced by a single instance of that letter followed by the number of occurrences of that 
letter. Then, the string thus obtained is further encrypted by reversing it.

Example 1:
Input:
s = "aabc“

Output: 
1c1b2a

Explanation: aabc
Step1: a2b1c1
Step2: 1c1b2a

Example 2:
Input:
s = "aaaaa“

Output: 
5a

Explanation: aaaaa
Step 1: a5
Step 2: 5a
"""

def encrypt_string(s):
    compressed = ""
    i = 0
    n = len(s)

    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            count += 1
            i += 1
        compressed += s[i] + str(count)
        i += 1

    return compressed[::-1]

s = input().strip()
print(encrypt_string(s))


# Decrypt Code Solution
"""
def decrypt_string(s):
    s = s[::-1] 
    decrypted = ""
    i = 0
    n = len(s)

    while i < n:
        char = s[i] 
        i += 1
        count = 0

        while i < n and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1

        decrypted += char * count

    return decrypted

s = input().strip()
print(decrypt_string(s))
"""


# When list of characters is given....
"""
class Solution(object):
    def compress(self, chars):
        compressed = []
        i = 0
        n = len(chars)

        while i < n:
            count = 1
            while i + 1 < n and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            
            compressed.append(chars[i])
            
            if count > 1:
                for digit in str(count):
                    compressed.append(digit)
            
            i += 1

        chars[:] = compressed
        return len(chars)
"""
