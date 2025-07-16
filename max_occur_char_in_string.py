from collections import Counter

def max_occuring_char(s):
    s = s.lower()  
    count = Counter(s)
    max_char = count.most_common(1)[0][0]
    return max_char

s = input()
result = max_occuring_char(s)
print(result)


"""
def max_occuring_char(s):
    freq = {}
    max_count = 0
    max_char = ''

    for char in s.lower(): 
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

        if freq[char] > max_count:
            max_count = freq[char]
            max_char = char

    return max_char

input_str = "Programminglife"
print("Output:", max_occuring_char(input_str))
"""