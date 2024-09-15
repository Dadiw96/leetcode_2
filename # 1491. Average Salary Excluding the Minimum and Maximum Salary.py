# 1491. Average Salary Excluding the Minimum and Maximum Salary

# Work
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. 
# Answers within 10^-5 of the actual answer will be accepted.

# Function Signature:
# def average(salary: List[int]) -> float:

# Input:
# - An array salary of length 3 <= salary.length <= 100 where 1000 <= salary[i] <= 10^6.
# - All the elements of salary are unique.

# Output:
# - A float representing the average salary excluding the minimum and maximum salary.

# Solution

def average(salary):
    #return (sum(salary)-max(salary) -min(salary))/(len(salary)-2)
    total, maxs, mins = 0, salary[0], salary[0]
    for s in salary:
        total += s
        mins = min(mins,s)
        maxs = max(maxs,s)
    r = (total-mins-maxs)/(len(salary)-2)
    return round(r,5)    
    
    
    
    
    
    
    
    
    
    
    
# Example 1:
# Input: salary = [4000, 3000, 1000, 2000]
# Output: 2500.00000
salary = [4000, 3000, 1000, 2000]
output = 2500.00000
print(f"Input: {salary}\nOutput: {output} ==>", average(salary))

# Example 2:
# Input: salary = [1000, 2000, 3000]
# Output: 2000.00000
salary = [1000, 2000, 3000]
output = 2000.00000
print(f"Input: {salary}\nOutput: {output} ==>", average(salary))

# Boundary Example 1:
# Input: salary = [6000, 5000, 4000, 3000, 2000, 1000]
# Output: 3500.00000
salary = [6000, 5000, 4000, 3000, 2000, 1000]
output = 3500.00000
print(f"Input: {salary}\nOutput: {output} ==>", average(salary))

# Boundary Example 2:
# Input: salary = [8000, 9000, 2000, 3000, 6000, 1000]
# Output: 4750.00000
salary = [8000, 9000, 2000, 3000, 6000, 1000]
output = 4750.00000
print(f"Input: {salary}\nOutput: {output} ==>", average(salary))