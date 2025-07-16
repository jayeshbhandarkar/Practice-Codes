"""
Before the outbreak of corona virus to the world, a meeting happened in a room in Wuhan. A person who attended that meeting had COVID-19 
and no one in the room knew about it! So everyone started shaking hands with everyone else in the room as a gesture of respect and after 
meeting unfortunately every one got infected! Given the fact that any two persons shake hand exactly once, Can you tell the total count of 
handshakes happened in that meeting?

Input Format:
The first line of contains the number of test cases T, T lines follow.
Each line contains an integer n, the total number of people attended that meeting.

Output Format:
Print the number of handshakes for each test-case in a new line.

Constraints:
1 <= T <= 1000
0 < N < 106

Input:
2
1
2

Output:
0
1
"""

def count_handshakes(test_cases):
    results = []
    for N in test_cases:
        handshakes = (N * (N - 1)) // 2
        results.append(str(handshakes))
    print("\n".join(results))  
    
T = int(input().strip())
test_cases = [int(input().strip()) for _ in range(T)]
count_handshakes(T, test_cases)
