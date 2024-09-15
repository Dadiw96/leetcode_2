#682. Baseball Game

#Work
#You are keeping scores for a baseball game with strange rules.
#The game consists of several rounds, where each round is represented by a string:
#1. An integer x represents the score of a round.
#2. A "+" represents the sum of the last two scores.
#3. A "D" represents doubling the last score.
#4. An "C" represents invalidating the last score.

#Given a list of strings representing the rounds, return the sum of the scores.

#Rozwiązanie

def calPoints(ops):
    r = []
    for o in ops:            
        if o == "D":
            r.append(r[-1]*2)     
        elif o == "C":
            r.pop()
        elif o == "+":
             r.append(r[-1] +r[-2])
        else:
            r.append(int(o))
    return sum(r)  
            

#Example 1:
#Input: ops = ["5","2","C","D","+"]
#Output: 30
ops = ["5", "2", "C", "D", "+"]
output = 30
print(f"#Example 1:\nInput: ops = {ops}\nOutput: {output} ==>", calPoints(ops))

#Example 2:
#Input: ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
output = 27
print(f"#Example 2:\nInput: ops = {ops}\nOutput: {output} ==>", calPoints(ops))

#Example 3:
#Input: ops = ["1"]
#Output: 1
ops = ["1"]
output = 1
print(f"#Example 3:\nInput: ops = {ops}\nOutput: {output} ==>", calPoints(ops))

#Boundary Example 1:
#Input: ops = []  # Empty list
#Output: 0
ops = []
output = 0
print(f"#Boundary Example 1:\nInput: ops = {ops}\nOutput: {output} ==>", calPoints(ops))


#Boundary Example 2:
#Input: ops = ["5","5","D","D","+"]
#Output: 70
ops = ["5", "5", "D", "D", "+"]
output = 70
print(f"#Boundary Example 2:\nInput: ops = {ops}\nOutput: {output} ==>", calPoints(ops))