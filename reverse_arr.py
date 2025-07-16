# Using Python Built-in Reverse Function

"""
def reverse_array(arr):
    arr.reverse()
    return arr

print(reverse_array([5, 4, 3, 2, 1]))  
print(reverse_array([10, 20, 30, 40]))  
"""

# ---------------------------------------------------------------------------

# Using Python Slicing

def reverse_array(arr):
    return arr[::-1]

print(reverse_array([5, 4, 3, 2, 1]))  
print(reverse_array([10, 20, 30, 40]))
