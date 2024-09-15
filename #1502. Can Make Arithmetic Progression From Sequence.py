#1502. Can Make Arithmetic Progression From Sequence

#Work
#A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
#Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

#Rozwiązanie

def canMakeArithmeticProgression(arr):
    arr = sorted(arr)
    val=arr[1]-arr[0]
    for n in range(2,len(arr)):
        if val != arr[n] - arr[n-1]:
            return False
    return True
    
            
#Example 1:
#Input: arr = [3,5,1]
#Output: True
arr = [3, 5, 1]
output = True
print(f"#Example 1:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))

#Example 2:
#Input: arr = [1,2,4]
#Output: False
arr = [1, 2, 4]
output = False
print(f"#Example 2:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))



#Boundary Example 2:
#Input: arr = [0, 0, 0, 0]  # All elements are the same
#Output: True (trivial progression)
arr = [0, 0, 0, 0]
output = True
print(f"#Boundary Example 2:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))

#Boundary Example 3:
#Input: arr = [2,4,6,8,10]  # Already an arithmetic progression
#Output: True
arr = [2, 4, 6, 8, 10]
output = True
print(f"#Boundary Example 3:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))

#Boundary Example 4:
#Input: arr = [10, 5, 0, -5, -10]  # Arithmetic progression with negative difference
#Output: True
arr = [10, 5, 0, -5, -10]
output = True
print(f"#Boundary Example 4:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))

#Boundary Example 5:
#Input: arr = [1,3,3]  # Repeated element breaks the progression
#Output: False
arr = [1, 3, 3]
output = False
print(f"#Boundary Example 5:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))

#Boundary Example 6:
#Input: arr = [1,3]  
#Output: False
arr = [1, 3, ]
output = True
print(f"#Boundary Example 6:\nInput: arr = {arr}\nOutput: {output} ==>", canMakeArithmeticProgression(arr))