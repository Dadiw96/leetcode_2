#58. Length of Last Word

#Work
#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

#Rozwiązanie

def lengthOfLastWord(s):
    s = s.strip()
    return len(s[s.rfind(" ")+1:])

#Example 1:
#Input: s = "Hello World"
#Output: 5
s = "Hello World   "
output = 5
print(f"#Example 1:\nInput: s = '{s}'\nOutput: {output} ==>", lengthOfLastWord(s))

#Example 2:
#Input: s = "   fly me   to   the moon  "
#Output: 4
s = "   fly me   to   the moon  "
output = 4
print(f"#Example 2:\nInput: s = '{s}'\nOutput: {output} ==>", lengthOfLastWord(s))

#Example 3:
#Input: s = "luffy is still joyboy"
#Output: 6
s = "luffy is still joyboy"
output = 6
print(f"#Example 3:\nInput: s = '{s}'\nOutput: {output} ==>", lengthOfLastWord(s))

#Boundary Example 1:
#Input: s = "a"
#Output: 1
s = "a"
output = 1
print(f"#Boundary Example 1:\nInput: s = '{s}'\nOutput: {output} ==>", lengthOfLastWord(s))

#Boundary Example 2:
#Input: s = "a "
#Output: 1
s = "a "
output = 1
print(f"#Boundary Example 2:\nInput: s = '{s}'\nOutput: {output} ==>", lengthOfLastWord(s))

#Boundary Example 3:
#Input: s = "    "  # Empty after trimming
#Output: 0
s = "    "
output = 0
print(f"#Boundary Example 3:\nInput: s = '{s}'\nOutput: {output} ==>", lengthOfLastWord(s))