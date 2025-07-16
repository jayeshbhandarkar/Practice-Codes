"""
def find_largest(arr):
    return max(arr) if arr else None

print(find_largest([2,5,1,3,0]))  
print(find_largest([8,10,5,7,9]))
"""

# ------------------------------------------------

"""
def find_largest(arr):
    return sorted(arr)[-1] if arr else None

print(find_largest([2,5,1,3,0]))  
print(find_largest([8,10,5,7,9]))
"""

# ------------------------------------------------

def find_largest(arr):
    if not arr:
        None
    
    largest = arr[-1]

    for num in arr:
        if num > largest:
            largest = num

    return largest

print(find_largest([2,5,1,3,0]))  
print(find_largest([8,10,5,7,9]))