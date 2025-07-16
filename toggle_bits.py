"""
Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit 
assignment problems before the lecture. Today he got one tricky question. The problem statement is “A positive 
integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after 
the most significant bit including the most significant bit. Print the positive integer value after toggling all 
bits”.

Constrains-
1<=N<=100

Example 1:
Input :
10  -> Integer

Output :
5   -> result- Integer

Explanation:
Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output
will print “5”.
"""

n = int(input())
#convert to binary
converted = bin(n)   

#Removes the '0b' prefix from the binary representation. '0b1010' → '1010'.
binary = converted[2:]

toggled = ""
for i in binary:
    if i == "0":
        toggled += "1"
    else:
        toggled += "0"

print(toggled)
decimal = int(toggled, 2)
print(decimal)


"""
import math
n=int(input())
k=(1<< int(math.log2(n))+1)-1
print(n^k)
"""