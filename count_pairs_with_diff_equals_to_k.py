def count_pairs_with_diff_k(arr, k):
    seen = set(arr)
    count = 0

    for num in seen:
        if num + k in seen:
            count += 1
        if num - k in seen and k != 0:  
            count += 1

    return count // 2 if k != 0 else count  

arr = [3, 2, 1, 5, 4]
k = 2
print(count_pairs_with_diff_k(arr, k))  


# If we want to displayed the pairs instead of the count

"""
def count_pairs_with_diff_k(arr, k):
    seen = set(arr)
    pairs = set()  # Use set to avoid duplicates

    for num in seen:
        if num + k in seen:
            pairs.add(tuple(sorted((num, num + k))))
        if num - k in seen and k != 0:
            pairs.add(tuple(sorted((num, num - k))))

    print(list(pairs))
    return len(pairs)

arr = [3, 2, 1, 5, 4]
k = 2
print(count_pairs_with_diff_k(arr, k))  
"""
