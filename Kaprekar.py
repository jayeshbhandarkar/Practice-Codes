def is_kaprekar(N):
    square = str(N * N) # Convert N^2 to a string
    length = len(square)
    
    for i in range(1, length): # Split at different positions
        left = square[:i] # Left part
        right = square[i:] # Right part

        # Convert to numbers (handle empty left part)
        left_num = int(left) if left else 0
        right_num = int(right) if right else 0
        
        if left_num + right_num == N:
            return "Yes"
    
    return "No"

T = int(input())
for _ in range(T):
    N = int(input())
    result = is_kaprekar(N)
    print(result)
