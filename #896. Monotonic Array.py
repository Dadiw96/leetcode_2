#896. Monotonic Array

#Work
#An array is monotonic if it is either monotone increasing or monotone decreasing.
#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
#An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#Given an integer array nums, return true if the given array is monotonic, or false otherwise.

#Rozwiązanie

def isMonotonic(nums):
    t=None
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            const = 1
        elif nums[i] < nums[i-1]:
            const = -1
        else:
            continue        
        if t == None :
            t = const
        elif t != const:
              return False 
    return True          
                 
                       

#Example 1:
#Input: nums = [1,2,2,3]
#Output: True
nums = [1, 2, 2, 3]
output = True
print(f"#Example 1:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Example 2:
#Input: nums = [6,5,4,4]
#Output: True
nums = [6, 5, 4, 4]
output = True
print(f"#Example 2:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Example 3:
#Input: nums = [1,3,2]
#Output: False
nums = [1, 3, 2]
output = False
print(f"#Example 3:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Boundary Example 1:
#Input: nums = [1]  # Single element
#Output: True
nums = [1]
output = True
print(f"#Boundary Example 1:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Boundary Example 2:
#Input: nums = [5,5,5,5]  # All elements are the same
#Output: True
nums = [5, 5, 5, 5]
output = True
print(f"#Boundary Example 2:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Boundary Example 3:
#Input: nums = [10,9,8,7,7,6]  # Monotonic decreasing array
#Output: True
nums = [10, 9, 8, 7, 7, 6]
output = True
print(f"#Boundary Example 3:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Boundary Example 4:
#Input: nums = [1,2,3,4,5]  # Monotonic increasing array
#Output: True
nums = [1, 2, 3, 4, 5]
output = True
print(f"#Boundary Example 4:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))

#Boundary Example 5:
#Input: nums = [1,3,2,4]  # Neither increasing nor decreasing
#Output: False
nums = [1, 3, 2, 4]
output = False
print(f"#Boundary Example 5:\nInput: nums = {nums}\nOutput: {output} ==>", isMonotonic(nums))