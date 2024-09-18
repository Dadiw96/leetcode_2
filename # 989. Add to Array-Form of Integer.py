# 989. Add to Array-Form of Integer

# Work
# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

# Function Signature:
# def addToArrayForm(num: List[int], k: int) -> List[int]:

# Input:
# - A list num of integers where 1 <= num.length <= 10^4.
# - Elements of the list are digits (0-9).
# - k is an integer where 0 <= k <= 10^4.

# Output:
# - Return the array-form of the integer after adding k to num.

# Solution

def addToArrayForm(num, k):
    total = []
    c = 0
    i = len(num)-1
    while i >= 0 or k > 0:
        if  i >= 0: 
            c += num[i]  
            i -= 1
        c += k % 10
        k //= 10
        total = [c % 10] + total
        c //= 10
    if c > 0:
            total = [c] + total      
    return "".join(total) 
        
            
            
            
            
            
           
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

# Example 1:
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
num = [1,2,0,0]
k = 34
output = [1,2,3,4]
print(f"Input: num = {num}, k = {k}\nOutput: {output} ==>", addToArrayForm(num, k))

# Example 2:
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
num = [2,7,4]
k = 181
output = [4,5,5]
print(f"Input: num = {num}, k = {k}\nOutput: {output} ==>", addToArrayForm(num, k))

# Example 3:
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
num = [2,1,5]
k = 806
output = [1,0,2,1]
print(f"Input: num = {num}, k = {k}\nOutput: {output} ==>", addToArrayForm(num, k))

# Boundary Example 1:
# Input: num = [9,9,9,9], k = 1
# Output: [1,0,0,0,0]
num = [9,9,9,9]
k = 1
output = [1,0,0,0,0]
print(f"Input: num = {num}, k = {k}\nOutput: {output} ==>", addToArrayForm(num, k))

# Boundary Example 2:
# Input: num = [0], k = 10000
# Output: [1,0,0,0,0]
num = [0]
k = 10000
output = [1,0,0,0,0]
print(f"Input: num = {num}, k = {k}\nOutput: {output} ==>", addToArrayForm(num, k))

# Boundary Example 3:
# Input: num = [12], k = 0
# Output: [1,2]
num = [12]
k = 0
output = [1,2]
print(f"Input: num = {num}, k = {k}\nOutput: {output} ==>", addToArrayForm(num, k))
