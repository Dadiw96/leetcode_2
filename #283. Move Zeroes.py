#283. Move Zeroes

#Work
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.

#Rozwiązanie

def moveZeroes(nums):
    k = 0
    for n in range(len(nums)):
        if nums[n] != 0:
            nums[k] = nums[n]
            k+=1
    for n in range(k,len(nums)):
        nums[n] = 0
    return nums

#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
nums = [0, 1, 0, 3, 12]
output = [1, 3, 12, 0, 0]
print(f"#Example 1:\nInput: nums = {nums}\nOutput: {output} ==>", moveZeroes(nums))

#Example 2:
#Input: nums = [0]
#Output: [0]
nums = [0]
output = [0]
print(f"#Example 2:\nInput: nums = {nums}\nOutput: {output} ==>", moveZeroes(nums))

#Boundary Example 1:
#Input: nums = [1, 0, 0, 0]  # Only one non-zero element
#Output: [1, 0, 0, 0]
nums = [1, 0, 0, 0]
output = [1, 0, 0, 0]
print(f"#Boundary Example 1:\nInput: nums = {nums}\nOutput: {output} ==>", moveZeroes(nums))

#Boundary Example 2:
#Input: nums = [0, 0, 0, 0]  # Only zeros
#Output: [0, 0, 0, 0]
nums = [0, 0, 0, 0]
output = [0, 0, 0, 0]
print(f"#Boundary Example 2:\nInput: nums = {nums}\nOutput: {output} ==>", moveZeroes(nums))

#Boundary Example 3:
#Input: nums = [1, 2, 3, 4, 5]  # No zeros
#Output: [1, 2, 3, 4, 5]
nums = [0,1, 2, 3, 4, 5]
output = [1, 2, 3, 4, 5,0]
print(f"#Boundary Example 3:\nInput: nums = {nums}\nOutput: {output} ==>", moveZeroes(nums))