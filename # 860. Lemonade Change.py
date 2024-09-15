# 860. Lemonade Change

# Work
# At a lemonade stand, each lemonade costs $5. 
# Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you don't have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, 
# return true if you can provide every customer with the correct change, or false otherwise.

# Function Signature:
# def lemonadeChange(bills: List[int]) -> bool:

# Input:
# - A list of integers bills where 1 <= bills.length <= 10^5 and bills[i] is either 5, 10, or 20.

# Output:
# - A boolean indicating whether it's possible to give the correct change to all customers.

# Solution

def lemonadeChange(bills):
    dic = {5:0, 10:0}
    for b in bills:
        if b == 5:               
            dic[5] += 1
        elif b == 10:
            if dic[5] < 0:
                return False
            else:
                dic[5] -= 1
                dic[10] += 1
        if b == 20:
            if dic[10] > 0 and dic[5] > 0:   
                dic[10] -= 1
                dic[5] -= 1
            elif dic[5] >= 3:
                dic[5] -= 3    
            else:
                return False       
    return True                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Example 1:
# Input: bills = [5,5,5,10,20]
# Output: True
bills = [5,5,5,10,20]
output = True
print(f"Input: {bills}\nOutput: {output} ==>", lemonadeChange(bills))

# Example 2:
# Input: bills = [5,5,10,10,20]
# Output: False
bills = [5,5,10,10,20]
output = False
print(f"Input: {bills}\nOutput: {output} ==>", lemonadeChange(bills))

# Example 3:
# Input: bills = [5,5,5,5,20,20,5,5,20,5]
# Output: False
bills = [5,5,5,5,20,20,5,5,20,5]
output = False
print(f"Input: {bills}\nOutput: {output} ==>", lemonadeChange(bills))

# Boundary Example 1:
# Input: bills = [5,10,5,10,5,20,5,10,5,20]
# Output: True
bills = [5,10,5,10,5,20,5,10,5,20]
output = True
print(f"Input: {bills}\nOutput: {output} ==>", lemonadeChange(bills))

# Boundary Example 2:
# Input: bills = [20,20,20]
# Output: False
bills = [20,20,20]
output = False
print(f"Input: {bills}\nOutput: {output} ==>", lemonadeChange(bills))