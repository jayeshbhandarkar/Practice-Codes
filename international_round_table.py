
"""
An international round table conference will be held in india. Presidents from all over the world representing their
respective countries will be attending the conference. The task is to find the possible number of ways(P) to make the 
N members sit around the circular table such that. The president and prime minister of India will always sit next to
each other.

Example 1:
Input :
4   -> Value of N(No. of members)

Output : 
12  -> Possible ways of seating the members

Explanation:
2  members should always be next to each other. So, 2 members can be in 2!ways. Rest of the members can be arranged
in (4-1)! ways.(1 is subtracted because the previously selected two members will be considered as single members now).
So total possible ways 4 members can be seated around the circular table 2*6= 12. Hence, output is 12.

Example 2:
Input:
10  -> Value of N(No. of members)

Output :
725760 -> Possible ways of seating the members 

Explanation:
2 members should always be next to each other. So, 2 members can be in 2! ways. Rest of the members can be arranged 
in (10-1)! Ways. (1 is subtracted because the previously selected two members will be considered as a single member 
now). So, total possible ways 10 members can be seated around a round table is 2*362880 = 725760 ways. Hence, output
is 725760.

The input format for testing -
The candidate has to write the code to accept one input, First input - Accept value of number of N(Positive integer 
number)

The output format for testing -
The output should be a positive integer number or print the message(if any) given in the problem statement(Check the
output in example 1, example2)

Constraints :
2<=N<=50
"""

n = int(input("Enter any Number: "))  
factorial = 1
i = n - 1  

while i > 0:
    factorial *= i
    i -= 1  

result = 2 * factorial  
print("\nPossible ways of seating the members:", result)


"""
n = int(input())
fact = [0] * (n + 1)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i
print(fact[n - 1] * 2)
"""


"""
import math
def seating_arrangements(n):
    if n < 2:
        return 0 
    return 2 * math.factorial(n - 1)

n = int(input())
print(seating_arrangements(n))
"""

# If instead of 2 we are given with 3 members should always be next to each other.

"""
n = int(input("Enter any Number: "))  
# Calculate (N-2)! using while loop
factorial = 1
i = n - 2  # Since we need (N-2)!

while i > 0:
    factorial *= i
    i -= 1  

# Multiply by 3! for the 3 members' internal arrangements
result = 6 * factorial  # 3! = 6
# Output the result
print("\nPossible ways of seating the members:", result)
"""