# 1523. Count Odd Numbers in an Interval Range

# Work
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Function Signature:
# def countOdds(low: int, high: int) -> int:

# Input:
# - Two integers low and high where 0 <= low <= high <= 10^9.

# Output:
# - The count of odd numbers between low and high (inclusive).

# Solution

def countOdds(low, high):
   odd = (high-low)//2
   if high % 2 == 1 or low %2 == 1:
          odd += 1
   return odd       
    
    
    
    
    
    
    
    
    
# Example 1:
# Input: low = 3, high = 7
# Output: 3
low, high = 3, 7
output = 3
print(f"Input: low = {low}, high = {high}\nOutput: {output} ==>", countOdds(low, high))

# Example 2:
# Input: low = 8, high = 10
# Output: 1
low, high = 8, 10
output = 1
print(f"Input: low = {low}, high = {high}\nOutput: {output} ==>", countOdds(low, high))

# Example 3:
# Input: low = 0, high = 1
# Output: 1
low, high = 0, 1
output = 1
print(f"Input: low = {low}, high = {high}\nOutput: {output} ==>", countOdds(low, high))

# Example 4:
# Input: low = 0, high = 4
# Output: 3
low, high = 0, 7
output = 4
print(f"Input: low = {low}, high = {high}\nOutput: {output} ==>", countOdds(low, high))

# Boundary Example 1:
# Input: low = 0, high = 0
# Output: 0
low, high = 0, 0
output = 0
print(f"Input: low = {low}, high = {high}\nOutput: {output} ==>", countOdds(low, high))

# Boundary Example 2:
# Input: low = 999999999, high = 1000000000
# Output: 1
low, high = 999999999, 1000000000
output = 1
print(f"Input: low = {low}, high = {high}\nOutput: {output} ==>", countOdds(low, high))