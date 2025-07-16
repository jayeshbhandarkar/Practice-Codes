"""
In a grand tournament, warriors stood in a line, each with a strength represented by a number. The rule was simple: A warrior could only 
be recognized as a champion if they were stronger than all who came before them. The first warrior always got the honor, but the rest had 
to prove their might.

Example:
Input 1:
Arr[] = [7, 4, 8, 2, 9]

Output 1:
3

Input 2:
Arr[] = [3, 4, 5, 8, 9]

Output 2:
5
"""

def find_Champion(arr):
    count = 0
    max_value = float('-inf')

    for champion in arr:
        if champion > max_value:
            count += 1
            max_value = champion
            
    return count

#arr = [7, 4, 8, 2, 9]
arr = [3, 4, 5, 8, 9]
result = find_Champion(arr)
print(result)
