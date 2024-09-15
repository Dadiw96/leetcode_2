#657. Robot Return to Origin

#Work
#A robot is located at the origin (0, 0) of a 2D grid.
#The robot can move up, down, left, or right.
#Given a string moves representing the robot's path, determine if the robot returns to the origin after executing all moves.

#Rozwiązanie

def judgeCircle(moves):
    dic = {"x":0,"y":0}
    for m in moves:            
        if m == "U":
            dic["y"] +=1     
        elif m == "D":    
            dic["y"] -=1
        elif m == "L":
            dic["x"] +=1
        elif m == "R":
            dic["x"] -=1
    print(dic["x"] ,dic["y"])
    return dic["x"] == 0 and dic["y"] == 0        
                    

#Example 1:
#Input: moves = "UD"
#Output: true
moves = "UD"
output = True
print(f"#Example 1:\nInput: moves = '{moves}'\nOutput: {output} ==>", judgeCircle(moves))

#Example 2:
#Input: moves = "LL"
#Output: false
moves = "LL"
output = False
print(f"#Example 2:\nInput: moves = '{moves}'\nOutput: {output} ==>", judgeCircle(moves))

#Example 3:
#Input: moves = "RRDD"
#Output: false
moves = "RRDD"
output = False
print(f"#Example 3:\nInput: moves = '{moves}'\nOutput: {output} ==>", judgeCircle(moves))

#Boundary Example 1:
#Input: moves = ""  # No moves
#Output: true
moves = ""
output = True
print(f"#Boundary Example 1:\nInput: moves = '{moves}'\nOutput: {output} ==>", judgeCircle(moves))

#Boundary Example 2:
#Input: moves = "UUDDLLRR"  # Returns to origin
#Output: true
moves = "UUDDLLRR"
output = True
print(f"#Boundary Example 2:\nInput: moves = '{moves}'\nOutput: {output} ==>", judgeCircle(moves))

#Boundary Example 3:
#Input: moves = "UURRDDLL "  
#Output: True
moves = "UURRDDLL"
output = True
print(f"#Boundary Example 3:\nInput: moves = '{moves}'\nOutput: {output} ==>", judgeCircle(moves))