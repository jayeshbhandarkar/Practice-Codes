"""
The Card Game Challenge -

You are participating in a unique card game where several cards are arranged in a row. Each card has a certain number
of points written on it. Your goal is to collect exactly K cards in such a way that your total score is maximized.
However, there's a catch! You can only pick cards from either the beginning or the end of the row in each step. Once 
a card is picked, it is removed, and you continue picking until you have exactly K cards. Your task is to determine 
the maximum score you can achieve by strategically picking cards.

Input Format:
The first line contains an integer N, the number of cards.
The second line contains N space-separated integers representing the points on each card.
The third line contains an integer K, the number of cards you must pick.

Output Format:
Print the maximum score that can be achieved by
picking exactly K cards optimally.
Input :
7
1 2 3 4 5 6 1
3
Output :
12
"""

def maxScore(k, cards):
    n = len(cards)
    left_sum = sum(cards[:k])
    max_score = left_sum
    right_sum = 0

    for i in range(1, k+1):
        right_sum += cards[-i]
        left_sum -= cards[k-i]
        max_score = max(max_score, left_sum + right_sum)

    return max_score

n = int(input())
cards = list(map(int, input().split()))
k = int(input())
result = maxScore(k, cards)
print(result)
