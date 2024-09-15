# 1672. Richest Customer Wealth

# Work
# You are given an array accounts where accounts[i] is the i-th customer's account, 
# and accounts[i][j] is the amount of money the i-th customer has in the j-th bank.

# Return the maximum wealth of any customer.

# The wealth of a customer is the sum of all amounts they have in all banks.

# Function Signature:
# def maximumWealth(accounts: List[List[int]]) -> int:

# Input:
# - A 2D list of integers accounts where 1 <= accounts.length <= 50 and 1 <= accounts[i].length <= 50.
# - Each account[i][j] (1 <= accounts[i][j] <= 100) represents the amount of money a customer has in a bank.

# Output:
# - The maximum wealth of any customer.

# Solution

def maximumWealth(accounts):
    m = -1
    for c in accounts:
        m = max(m,sum(c))
    return m    
        
        
        
        

# Example 1:
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
accounts = [[1,2,3],[3,2,1]]
output = 6
print(f"Input: {accounts}\nOutput: {output} ==>", maximumWealth(accounts))

# Example 2:
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
accounts = [[1,5],[7,3],[3,5]]
output = 10
print(f"Input: {accounts}\nOutput: {output} ==>", maximumWealth(accounts))

# Example 3:
# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17
accounts = [[2,8,7],[7,1,3],[1,9,5]]
output = 17
print(f"Input: {accounts}\nOutput: {output} ==>", maximumWealth(accounts))

# Boundary Example 1:
# Input: accounts = [[1]]
# Output: 1
accounts = [[1]]
output = 1
print(f"Input: {accounts}\nOutput: {output} ==>", maximumWealth(accounts))
