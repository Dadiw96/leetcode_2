#242. Valid Anagram

#Work
#Given two strings s and t, return true if t is an anagram of s and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Rozwiązanie

def isAnagram(s, t):
    return ("".join(reversed(s)))  == t 

#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: True
s = "anagram"
t = "margana"
output = True
print(f"#Example 1:\nInput: s = '{s}', t = '{t}'\nOutput: {output} ==>", isAnagram(s, t))

#Example 2:
#Input: s = "rat", t = "car"
#Output: False
s = "rat"
t = "car"
output = False
print(f"#Example 2:\nInput: s = '{s}', t = '{t}'\nOutput: {output} ==>", isAnagram(s, t))

#Boundary Example 1:
#Input: s = "a", t = "a"  # Single character match
#Output: True
s = "a"
t = "a"
output = True
print(f"#Boundary Example 1:\nInput: s = '{s}', t = '{t}'\nOutput: {output} ==>", isAnagram(s, t))

#Boundary Example 2:
#Input: s = "", t = ""  # Both strings are empty
#Output: True
s = ""
t = ""
output = True
print(f"#Boundary Example 2:\nInput: s = '{s}', t = '{t}'\nOutput: {output} ==>", isAnagram(s, t))

#Boundary Example 3:
#Input: s = "abc", t = "ab"  # Different lengths
#Output: False
s = "abc"
t = "ab"
output = False
print(f"#Boundary Example 3:\nInput: s = '{s}', t = '{t}'\nOutput: {output} ==>", isAnagram(s, t))

#Boundary Example 4:
#Input: s = "aabbcc", t = "abcabc"  # Both strings are anagrams
#Output: True
s = "aabbcc"
t = "abcabc"
output = True
print(f"#Boundary Example 4:\nInput: s = '{s}', t = '{t}'\nOutput: {output} ==>", isAnagram(s, t))