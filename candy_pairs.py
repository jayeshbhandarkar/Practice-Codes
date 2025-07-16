"""
Candy pairs -

You have a box of candies of different brands and different stres represented by the string candies. There are two 
sizes of candies produced by each brand which are small and large. Uppercase alphabets are used to represent large 
candies, while lowercase alphabets are used to represent small candies, If one brand is higher in alphabetical order 
than another, for example, C> B, then that brand is better. Therefore, Brand C is better than Brand B. Find the best 
candy pair in the box that is the best brand that has both small and large candies in the box, and return 0 if it 
isn't there. You are given an integer N where N represents the total number of candies in the box. You are given an 
array of candies representing the brand and type of candies in the box. Each candy is represented by an English 
alphabet where lowercase alphabets denote the small candies and uppercase alphabets denote the large candies.

Return the uppercase representation of the best brand that has both small and large candies in the box. If it is not 
there, return 0.

Function description -

Complete the Solve() function. This function takes the following 2 arguments and returns the answer.
Int(input())

N
10
G
11

N. Represents the total candies in the box candies): Represents the brand and type of candies in the box, each candy 
is represented by an English alphabet where lowercase alphabets denote the small candies and upper case alphabets 
denote the large candies

Input format for custom testing -

Note: Use this input format if you are testing against custom input or writing code in a language where we don't 
provide boilerplate code.
The first line contains an integer N denoting the total number of candies in the box.
The second line contains a string of size N representing the brand and type of candies in the box.

Output format -
Return the uppercase representation of the best brand candy pair. If not available, then 0.

Explanation -
int(inport())

Given
N-6
candiibBdCcD

Approach -
There are three candy pairs (b. B) (c, C), and [d. D) in the box. Brand D is better than Brand B and Brand A. 
Therefore best brand candy pair is D.
"""

def Solve(N, candies):
    if N == 0 or not candies:
        return 0

    small_candies = set()
    large_candies = set()

    for candy in candies:
        if 'a' <= candy <= 'z':
            small_candies.add(candy.upper())
        elif 'A' <= candy <= 'Z':  
            large_candies.add(candy)

    common_brands = small_candies & large_candies
  
    if common_brands:
        return max(common_brands)
    else:
        return 0
