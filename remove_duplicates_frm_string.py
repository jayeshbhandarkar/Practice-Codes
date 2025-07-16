def remove_duplicates(arr):
    x = sorted(set(arr))
    print(x)

arr = ["apple", "banana", "orange", "banana", "apple", "grapes"]
remove_duplicates(arr)


"""
def remove_duplicates(s):
    result = ""
    seen = set()
    
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result

input_str = input("Enter a string: ")
output_str = remove_duplicates(input_str)
print("String after removing duplicates:", output_str)

"""