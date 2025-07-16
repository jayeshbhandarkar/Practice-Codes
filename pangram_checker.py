def is_pangram(s):
    s = s.lower()
    letters = set()

    for char in s:
        if char.isalpha():
            letters.add(char)

    return "Yes" if len(letters) == 26 else "No"

input1 = "The quick brown fox jumps over the lazy dog."
input2 = "Coding gives you superpowers"

print(is_pangram(input1))
print(is_pangram(input2))
