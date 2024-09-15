#1822. Sign of the Product of an Array

#Work
#There is a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).

#Rozwiązanie

def arraySign(nums):
    l=1
    
    for n in nums:
        if n == 0:
            return 0
        elif n < 0:
            l*=-1
    return l          

#Example 1:
#Input: nums = [-1,-2,-3,-4,3,2,1]
#Output: 1
nums = [-1, -2, -3, -4, 3, 2, 1]
output = 1
print(f"#Example 1:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))

#Example 2:
#Input: nums = [1,5,0,2,-3]
#Output: 0
nums = [1, 5, 0, 2, -3]
output = 0
print(f"#Example 2:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))

#Example 3:
#Input: nums = [-1,1,-1,1,-1]
#Output: -1
nums = [-1, 1, -1, 1, -1]
output = -1
print(f"#Example 3:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))

#Boundary Example 1:
#Input: nums = [0]  # Single zero
#Output: 0
nums = [0]
output = 0
print(f"#Boundary Example 1:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))

#Boundary Example 2:
#Input: nums = [1,2,3,4,5]  # All positive numbers
#Output: 1
nums = [1, 2, 3, 4, 5]
output = 1
print(f"#Boundary Example 2:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))

#Boundary Example 3:
#Input: nums = [-1, -1, -1, -1]  # All negative numbers
#Output: 1 (because product of even number of negative numbers is positive)
nums = [-1, -1, -1, -1]
output = 1
print(f"#Boundary Example 3:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))

#Boundary Example 4:
#Input: nums = [-1, -1, -1]  # Odd number of negative numbers
#Output: -1
nums = [-1, -1, -1]
output = -1
print(f"#Boundary Example 4:\nInput: nums = {nums}\nOutput: {output} ==>", arraySign(nums))