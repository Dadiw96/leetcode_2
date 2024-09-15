# 1232. Check If It Is a Straight Line

# Work
# You are given an array coordinates, where coordinates[i] = [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY-plane.

# Function Signature:
# def checkStraightLine(coordinates: List[List[int]]) -> bool:

# Input:
# - A list of lists, coordinates, where 2 <= coordinates.length <= 1000 and coordinates[i].length == 2.
# - Coordinates consist of integer values between -10^4 and 10^4.

# Output:
# - A boolean indicating whether all the points lie on a straight line.

# Solution

def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True
    
    (x0, y0) = coordinates[0]
    (x1, y1) = coordinates[1]
    
    for i in range(2, len(coordinates)):
        (x2, y2) = coordinates[i]
        if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
            return False
    
    return True

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
output = True
print(f"Input: {coordinates}\nOutput: {output} ==>", checkStraightLine(coordinates))

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: False
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
output = False
print(f"Input: {coordinates}\nOutput: {output} ==>", checkStraightLine(coordinates))

# Boundary Example 1:
# Input: coordinates = [[0,0],[0,1],[0,-1]]
# Output: True
coordinates = [[0,0],[0,1],[0,-1]]
output = True
print(f"Input: {coordinates}\nOutput: {output} ==>", checkStraightLine(coordinates))

# Boundary Example 2:
# Input: coordinates = [[1,2],[1,3],[1,4],[1,5]]
# Output: True
coordinates = [[1,2],[1,3],[1,4],[1,5]]
output = True
print(f"Input: {coordinates}\nOutput: {output} ==>", checkStraightLine(coordinates))

# Boundary Example 3:
# Input: coordinates = [[1,0],[0,0],[1,1],[2,2]]
# Output: False
coordinates = [[1,0],[0,0],[1,1],[2,2]]
output = False
print(f"Input: {coordinates}\nOutput: {output} ==>", checkStraightLine(coordinates))