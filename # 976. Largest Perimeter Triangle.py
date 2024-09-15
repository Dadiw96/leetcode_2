# 976. Largest Perimeter Triangle

# Work
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
# formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# Function Signature:
# def largestPerimeter(nums: List[int]) -> int:

# Input:
# - A list of integers nums where 3 <= nums.length <= 10^4 and 1 <= nums[i] <= 10^6.

# Output:
# - The largest perimeter of a triangle, or 0 if no valid triangle can be formed.

# Solution

def largestPerimeter(nums):
    nums.sort(reverse = True)
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0    
        

# Example 1:
# Input: nums = [2,1,2]
# Output: 5
nums = [2,1,2]
output = 5
print(f"Input: {nums}\nOutput: {output} ==>", largestPerimeter(nums))

# Example 2:
# Input: nums = [1,2,1]
# Output: 0
nums = [1,2,1]
output = 0
print(f"Input: {nums}\nOutput: {output} ==>", largestPerimeter(nums))

# Example 3:
# Input: nums = [3,2,3,4]
# Output: 10
nums = [3,2,3,4]
output = 10
print(f"Input: {nums}\nOutput: {output} ==>", largestPerimeter(nums))

# Example 4:
# Input: nums = [3,6,2,3]
# Output: 8
nums = [3,6,2,3]
output = 8
print(f"Input: {nums}\nOutput: {output} ==>", largestPerimeter(nums))

# Boundary Example 1:
# Input: nums = [10,10,10]
# Output: 30
nums = [10,10,10]
output = 30
print(f"Input: {nums}\nOutput: {output} ==>", largestPerimeter(nums))

# Boundary Example 2:
# Input: nums = [1,2,10]
# Output: 0
nums = [1,2,10]
output = 0
print(f"Input: {nums}\nOutput: {output} ==>", largestPerimeter(nums))