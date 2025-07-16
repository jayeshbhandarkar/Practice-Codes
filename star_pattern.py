"""
Print a diamond pattern where each row contains increasing numbers in the first half and decreasing numbers in the 
second half.

Example (N = 4):

   1
  121
 12321
1234321
 12321
  121
   1

"""

def print_diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        
        for j in range(1, i + 1):
            print(j, end="")
        
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()

    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        
        for j in range(1, i + 1):
            print(j, end="")
        
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()

print_diamond(4)
