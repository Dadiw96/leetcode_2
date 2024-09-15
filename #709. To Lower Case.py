#709. To Lower Case

#Work
#Implement function toLowerCase() that has a string input s, and returns the same string with all characters converted to lowercase.

#Rozwiązanie

def toLowerCase(s):
    for i in range(len(s)):
        c = ord(s[i])
        if c > 64 and c < 91:
            s = s[:i]+ chr(c+32) + s[i+1:]
    return s         






#Example 1:
#Input: s = "Hello"
#Output: "hello"
s = "Hello"
output = "hello"
print(f"#Example 1:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s))

#Example 2:
#Input: s = "here"
#Output: "here"
s = "here"
output = "here"
print(f"#Example 2:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s))

#Example 3:
#Input: s = "LOVELY"
#Output: "lovely"
s = "LOVELY"
output = "lovely"
print(f"#Example 3:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s))

#Boundary Example 1:
#Input: s = "a"  # Single lowercase letter
#Output: "a"
s = "a"
output = "a"
print(f"#Boundary Example 1:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s))

#Boundary Example 2:
#Input: s = "A"  # Single uppercase letter
#Output: "a"
s = "A"
output = "a"
print(f"#Boundary Example 2:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s))

#Boundary Example 3:
#Input: s = "123"  # Digits only
#Output: "123"
s = "123"
output = "123"
print(f"#Boundary Example 3:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s))

#Boundary Example 4:
#Input: s = ""  # Empty string
#Output: ""
s = ""
output = ""
print(f"#Boundary Example 4:\nInput: s = '{s}'\nOutput: '{output}' ==>", toLowerCase(s)) 