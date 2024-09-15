#66. Plus One

#Work
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
#The digits are ordered from most significant to least significant in left-to-right order.
#The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.

#Rozwiązanie

def plusOne(digits):
    for i in range(1,len(digits)+1):
        if digits[-i] < 9:
            digits[-i] +=1
            print(digits[-i])
            return digits
        digits[-i] = 0
    return [1] + digits        
    
    
    

#Example 1:
#Input: digits = [1,2,3]
#Output: [1,2,4]
digits = [1, 2, 3]
output = [1, 2, 4]
print(f"#Example 1:\nInput: digits = {digits}\nOutput: {output} ==>", plusOne(digits))

#Example 2:
#Input: digits = [4,3,2,1]
#Output: [4,3,2,2]
digits = [4, 3, 2, 1]
output = [4, 3, 2, 2]
print(f"#Example 2:\nInput: digits = {digits}\nOutput: {output} ==>", plusOne(digits))

#Example 3:
#Input: digits = [9]
#Output: [1,0]
digits = [9]
output = [1, 0]
print(f"#Example 3:\nInput: digits = {digits}\nOutput: {output} ==>", plusOne(digits))

#Boundary Example 1:
#Input: digits = [0]  # Single zero
#Output: [1]
digits = [0]
output = [1]
print(f"#Boundary Example 1:\nInput: digits = {digits}\nOutput: {output} ==>", plusOne(digits))

#Boundary Example 2:
#Input: digits = [9,9,9]  # All nines
#Output: [1,0,0,0]
digits = [9, 9, 9]
output = [1, 0, 0, 0]
print(f"#Boundary Example 2:\nInput: digits = {digits}\nOutput: {output} ==>", plusOne(digits))

#Boundary Example 3:
#Input: digits = [1,9,9]  # Last two digits are nines
#Output: [2,0,0]
digits = [1, 9, 9]
output = [2, 0, 0]
print(f"#Boundary Example 3:\nInput: digits = {digits}\nOutput: {output} ==>", plusOne(digits))