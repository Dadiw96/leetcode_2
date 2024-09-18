# 73. Set Matrix Zeroes

# Work
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Function Signature:
# def setZeroes(matrix: List[List[int]]) -> None:

# Input:
# - A matrix of integers where 1 <= matrix.length, matrix[0].length <= 200.
# - Elements of the matrix are integers between -2^31 and 2^31 - 1.

# Output:
# - Modify the matrix in place. Do not return anything.

# Solution

def setZeroes(matrix):
    col, row = len(matrix), len(matrix[0])
    #spr czy w pierwszym wierszu lub kolumnie sa zera
    First_Col_zero = any(matrix[i][0] == 0  for i in range(col)) 
    First_Row_zero = any(matrix[0][j] == 0 for j in range(row))
    
    #usawienie 0 w pierwszym wierszu i kolumnie wszedzie tam gdzie sa 1
    for c in range(1,col):
        for r in range(1,row):
            if matrix[c][r] == 0:
                matrix[0][r] = 0
                matrix[c][0] = 0               
                      
    #zmiana tablicy dla elementow poza 1 row i 1 col
    for c in range(1,col):
        for r in range(1,row):
            if matrix[c][0] == 0 or matrix[0][r ] == 0:
                    matrix[c][r] = 0
    
    #ustawienie pierwszej kolumny i wiersza
    if First_Col_zero:
        for c in range(col):
            matrix[c][0] = 0
    if First_Row_zero:
       for r in range(row):
           matrix[0][r] = 0

    
    
def printMatrix(matrix = None):
    
    print("/n Przed trans")
    for m in matrix:
        print(m)
    
    setZeroes(matrix)
    
    print("/n Po trans")
    for m in matrix:
        print(m)
    
    
    
    
    
    
      
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]
output = [[1,0,1],[0,0,0],[1,0,1]]
print(output, " ==>", printMatrix(matrix))

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(f"Input: {matrix}\nOutput: {output} ==>", printMatrix(matrix))

# Boundary Example 1:
# Input: matrix = [[1,2,3],[4,0,6],[7,8,9]]
# Output: [[1,0,3],[0,0,0],[7,0,9]]
matrix = [[1,2,3],[4,0,6],[7,8,9]]
output = [[1,0,3],[0,0,0],[7,0,9]]
print(f"Input: {matrix}\nOutput: {output} ==>", printMatrix(matrix))

# Boundary Example 2:
# Input: matrix = [[0,1],[2,3]]
# Output: [[0,0],[0,3]]
matrix = [[0,1],[2,3]]
output = [[0,0],[0,3]]
print(f"Input: {matrix}\nOutput: {output} ==>", printMatrix(matrix))

# Boundary Example 3:
# Input: matrix = [[1,0,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [[0,0,0,0],[5,0,7,8],[9,0,11,12]]
matrix = [[1,0,3,4],
                [5,6,7,8],
                [9,10,11,12]]
output = [[0,0,0,0],[5,0,7,8],[9,0,11,12]]
print(f"Input: {matrix}\nOutput: {output} ==>", printMatrix(matrix))

