def find_second_smallest_largest(arr):
    if len(arr) < 2:
        return -1, -1  

    unique_sorted_arr = sorted(set(arr)) 
    if len(unique_sorted_arr) < 2:
        return -1, -1 

    second_smallest = unique_sorted_arr[1]
    second_largest = unique_sorted_arr[-2]
    return second_smallest, second_largest

print(find_second_smallest_largest([2, 5, 1, 3, 0]))  
print(find_second_smallest_largest([8, 10, 5, 7, 9])) 
print(find_second_smallest_largest([5]))            
print(find_second_smallest_largest([2, 2, 2, 2]))    
