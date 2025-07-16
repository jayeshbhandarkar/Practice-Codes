def rotateMatrix90(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()

    return matrix

matrix = [list(map(int, row.strip("[]").split(","))) for row in input().strip("[] ").split("], [")]
answer = rotateMatrix90(matrix)
print(answer)


# ------------------------------------------------------------------------------------------

# Test Case:
# Input: matrix = [[1,2,3], [4,5,6], [7,8,9]]
# Output: [7,4,1]
#         [8,5,2]
#         [9,6,3]

# ------------------------------------------------------------------------------------------

"""
def rotateMatrix90(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()

matrix = [list(map(int, row.strip("[]").split(","))) for row in input().strip("[] ").split("], [")]
rotateMatrix90(matrix)

for row in matrix:
    print(row)
"""