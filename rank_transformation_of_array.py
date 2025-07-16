def rank_transform(arr):
    count = sorted(set(arr))     
    rank_dict = {}  
    rank = 1

    for i in count:
        rank_dict[i] = rank
        rank += 1

    result = [] 
    
    for i in arr:
        result.append(rank_dict[i])
    
    return result

arr = list(map(int, input().split()))
print(*rank_transform(arr))
