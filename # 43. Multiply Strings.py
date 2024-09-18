# 43. Multiply Strings

# Work
# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integers directly.

# Function Signature:
# def multiply(num1: str, num2: str) -> str:

# Input:
# - Two strings num1 and num2 consisting of digits (0-9) where 1 <= num1.length, num2.length <= 200.
# - num1 and num2 do not contain any leading zeros, except the number zero itself.

# Output:
# - Return the product of num1 and num2 as a string.

# Solution

def multiply(num1, num2):
    t, d = 0, 1 
    i, l = len(num1) - 1, len(num2) - 1
    while i >= 0:
        j, c, m = l, 0, 1      
        while j >= 0: 
            c += m1(num1[i], num2[j])*m
            m *= 10
            j -= 1        
        t += c * d      
        d *= 10             
        i -= 1
        print(t)
    return total(t)
    
def total(t):
    total = []
    while t != 0:     
         total = [str(t%10)] + total
         t //= 10
    return "".join(total)
         
def m1(i,j):
     dig1 = ord(i) - ord("0")
     dig2 = ord(j) - ord("0")
     return dig1 * dig2
     











#tututu             
         
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
num1 = "123"
num2 =  "6"
output = "738"
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
num1 = "123"
num2 = "50" 
output = "6150" 
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
num1 = "123"
num2 = "400" 
output = "49200"
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
num1 = "123"
num2 = "456"
output = "56088"
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

# Boundary Example 1:
# Input: num1 = "0", num2 = "456"
# Output: "0"
num1 = "0"
num2 = "456"
output = "0"
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

# Boundary Example 2:
# Input: num1 = "999", num2 = "999"
# Output: "998001"
num1 = "999"
num2 = "999"
output = "998001"
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

# Boundary Example 3:
# Input: num1 = "1", num2 = "123456789"
# Output: "123456789"
num1 = "1"
num2 = "123456789"
output = "123456789"
print(f"Input: num1 = {num1}, num2 = {num2}\nOutput: {output} ==>", multiply(num1, num2))

