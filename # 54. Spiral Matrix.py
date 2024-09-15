# 54. Spiral Matrix

# Work
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Function Signature:
# def spiralOrder(matrix: List[List[int]]) -> List[int]:

# Input:
# - A 2D list of integers matrix where 1 <= matrix.length <= 10^4 and 1 <= matrix[i].length <= 10^4.
# - The matrix will have at most 10^4 elements.

# Output:
# - A list of integers representing the elements of the matrix in spiral order.

# Solution

def spiralOrder(matrix):
    col, row = len(matrix[0]), len(matrix)
    a=col*row
    l, r, t, b = 0, col-1, 0, row-1  
    result=[]
    while l <= r and t <= b:
        for i in range(l,r+1):
            result.append(matrix[t][i])
        t += 1    
        for j in range(t,b+1):
            result.append(matrix[j][r])
        r -= 1    
        if t <= b:
            for  i in range(r, l-1, -1):
                 result.append(matrix[b][i])      
            b -= 1    
        if l <= r:
            for j in range(b,t-1,-1):
                result.append(matrix[j][l]) 
            l += 1        
    
    
    return result
    
    
    
    
   
                                    
                                        
                                            
                                                
                                                        

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = [1,2,3,6,9,8,7,4,5]
print(f"Input: {matrix}\nOutput: {output} ==>", spiralOrder(matrix))
print(output== spiralOrder(matrix))

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
output = [1,2,3,4,8,12,11,10,9,5,6,7]
print(f"Input: {matrix}\nOutput: {output} ==>", spiralOrder(matrix))
print(output== spiralOrder(matrix))

# Example 3:
# Input: matrix = [[1]]
# Output: [1]
matrix = [[1]]
output = [1]
print(f"Input: {matrix}\nOutput: {output} ==>", spiralOrder(matrix))
print(output== spiralOrder(matrix))

# Boundary Example 1:
# Input: matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
Output: [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
output = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
print(f"Input: {matrix}\nOutput: {output} ==>", spiralOrder(matrix))
print(output== spiralOrder(matrix))

# Boundary Example 2:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# Output: [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11]
matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
output = [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11]
print(f"Input: {matrix}\nOutput: {output} ==>", spiralOrder(matrix))
print(output== spiralOrder(matrix))