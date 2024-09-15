# 67. Add Binary

# Work
# Given two binary strings a and b, return their sum as a binary string.

# Function Signature:
# def addBinary(a: str, b: str) -> str:

# Input:
# - Two binary strings a and b, where 1 <= a.length, b.length <= 10^4.
# - Each string consists of only '0' and '1' characters.

# Output:
# - The sum of the two binary strings, represented as a binary string.

# Solution

def addBinary(a: str, b: str) -> str:
    r = []
    
                

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
a, b = "11", "1"
output = "100"
print(f"Input: a = '{a}', b = '{b}'\nOutput: '{output}' ==>", addBinary(a, b))

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
a, b = "1010", "1011"
output = "10101"
print(f"Input: a = '{a}', b = '{b}'\nOutput: '{output}' ==>", addBinary(a, b))

# Boundary Example 1:
# Input: a = "0", b = "0"
# Output: "0"
a, b = "0", "0"
output = "0"
print(f"Input: a = '{a}', b = '{b}'\nOutput: '{output}' ==>", addBinary(a, b))

# Boundary Example 2:
# Input: a = "111", b = "111"
# Output: "1110"
a, b = "111", "111"
output = "1110"
print(f"Input: a = '{a}', b = '{b}'\nOutput: '{output}' ==>", addBinary(a, b))

# Boundary Example 3:
# Input: a = "10101010101010101010", b = "11011011011011011011"
# Output: "100000000000000000001"
a, b = "10101010101010101010", "11011011011011011011"
output = "100000000000000000001"
print(f"Input: a = '{a}', b = '{b}'\nOutput: '{output}' ==>", addBinary(a, b))