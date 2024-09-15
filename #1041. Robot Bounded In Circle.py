#1041. Robot Bounded In Circle

#Work
#On an infinite plane, a robot initially stands at (0, 0) and faces north.
#The robot can receive a sequence of commands:
#- "G": Move forward one unit.
#- "L": Turn left 90 degrees.
#- "R": Turn right 90 degrees.

#Given a string commands representing the sequence of commands, determine if the robot is bounded in a circle.

#Rozwiązanie

def isRobotBounded(commands):
    position=[0,0]
    direction = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    i = 0
    for _ in range(4): 
        for c in commands:            
            if c == "G":
                position[0] += direction[i][0]
                position[1] += direction[i][1]    
            elif c == "L":
                i = (i - 1) % 4
            elif c == "R":
                i = (i + 1) % 4   
    if position == [0,0] or i != 0:
        return True         
    return False        
                
                
                
                

#Example 1:
#Input: commands = "GGLLGG"
#Output: true
commands = "GGLLGG"
output = True
print(f"#Example 1:\nInput: commands = '{commands}'\nOutput: {output} ==>", isRobotBounded(commands))

#Example 2:
#Input: commands = "GG"
#Output: false
commands = "GG"
output = False
print(f"#Example 2:\nInput: commands = '{commands}'\nOutput: {output} ==>", isRobotBounded(commands))

#Example 3:
#Input: commands = "GL"
#Output: true
commands = "GL"
output = True
print(f"#Example 3:\nInput: commands = '{commands}'\nOutput: {output} ==>", isRobotBounded(commands))

#Boundary Example 1:
#Input: commands = ""  # No commands
#Output: true
commands = ""
output = True
print(f"#Boundary Example 1:\nInput: commands = '{commands}'\nOutput: {output} ==>", isRobotBounded(commands))

#Boundary Example 2:
#Input: commands = "L"  # Turning left only
#Output: true
commands = "L"
output = True
print(f"#Boundary Example 2:\nInput: commands = '{commands}'\nOutput: {output} ==>", isRobotBounded(commands))

#Boundary Example 3:
#Input: commands = "RGRGRGRG"  # Making full turns without movement
#Output: true
commands = "RGRGRGRG"
output = True
print(f"#Boundary Example 3:\nInput: commands = '{commands}'\nOutput: {output} ==>", isRobotBounded(commands))