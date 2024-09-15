# 1572. Matrix Diagonal Sum

# Work
# You are given a square matrix mat of size n x n.
# Return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# Function Signature:
# def diagonalSum(mat: List[List[int]]) -> int:

# Input:
# - A 2D list of integers mat where 1 <= mat.length == mat[i].length <= 100 and 1 <= mat[i][j] <= 100.

# Output:
# - The sum of all diagonal elements, counting each element only once if it is both on the primary and secondary diagonal.

# Solution

def diagonalSum(mat):
    l=len(mat[0])-1
    r=0
    for i,m in enumerate(mat):
        if i == l:
            r+=m[i]
        else:
            r+=m[i]+m[l]
        l-=1
        
    return r
    
   
        
        

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 25
mat = [[1,2,3],[4,5,6],[7,8,9]]
output = 25
print(f"Input: {mat}\nOutput: {output} ==>", diagonalSum(mat))

# Example 2:
# Input: mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# Output: 8
mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
output = 8
print(f"Input: {mat}\nOutput: {output} ==>", diagonalSum(mat))

# Example 3:
# Input: mat = [[5]]
# Output: 5
mat = [[5]]
output = 5
print(f"Input: {mat}\nOutput: {output} ==>", diagonalSum(mat))

# Example 4:
# Input: mat = [[1, 2, 3, 4, 5],
#                       [6, 7, 8, 9, 10],
#                       [11, 12, 13, 14, 15],
#                       [16, 17, 18, 19, 20],
#                        [21, 22, 23, 24, 25]]
# Output: 117
mat = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
output = 117 
print(f"Input: {mat}\nOutput: {output} ==>", diagonalSum(mat))


# Boundary Example 2:
# Input: mat = [[1]]
# Output: 1
mat = [[1]]
output = 1
print(f"Input: {mat}\nOutput: {output} ==>", diagonalSum(mat))