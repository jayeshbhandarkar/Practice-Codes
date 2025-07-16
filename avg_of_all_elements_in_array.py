"""
def avg_of_elements_in_array(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    avg = sum / len(arr)
    return avg
    
arr = [1,2,3,4,5]
arr1 = [1,2,1,1,5,1]
print(avg_of_elements_in_array(arr))
print(avg_of_elements_in_array(arr1))
"""

# Using Built-in Functions
def findAverage(arr):
    return round(sum(arr) / len(arr), 1)

arr = [1,2,3,4,5]
arr1 = [1,2,1,1,5,1]
print(findAverage(arr))
print(findAverage(arr1))
