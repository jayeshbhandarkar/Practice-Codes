def find_smallest(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

print(find_smallest([2,5,1,3,0]))  
print(find_smallest([8,10,5,7,9]))  


# ------------------------------------------------

"""
def find_smallest(arr):
    return min(arr) if arr else None 

print(find_smallest([2,5,1,3,0]))  
print(find_smallest([8,10,5,7,9]))
"""

# ------------------------------------------------

"""
def find_smallest(arr):
    return sorted(arr)[0] if arr else None

print(find_smallest([2,5,1,3,0]))  
print(find_smallest([8,10,5,7,9]))
"""