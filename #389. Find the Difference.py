#389. Find the Difference

#Work
#You are given two strings s and t. String t is generated by randomly shuffling string s 
#and then adding one more letter at a random position.
#Return the letter that was added to t.

#Rozwiązanie

def findTheDifference(s, t):
    for char in t:
        if s.count(char) != t.count(char):
            return char

#Example 1:
#Input: s = "abcd", t = "abcde"
#Output: "e"
s = "abcd"
t = "abcde"
output = "e"
print(f"#Example 1:\nInput: s = {s}, t = {t}\nOutput: {output} ==>", findTheDifference(s, t))

#Example 2:
#Input: s = "", t = "y"
#Output: "y"
s = ""
t = "y"
output = "y"
print(f"#Example 2:\nInput: s = {s}, t = {t}\nOutput: {output} ==>", findTheDifference(s, t))

#Example 3:
#Input: s = "a", t = "aa"
#Output: "a"
s = "a"
t = "aa"
output = "a"
print(f"#Example 3:\nInput: s = {s}, t = {t}\nOutput: {output} ==>", findTheDifference(s, t))

#Boundary Example 1:
#Input: s = "abc", t = "cabd"  # Randomly added 'd'
#Output: "d"
s = "abc"
t = "cabd"
output = "d"
print(f"#Boundary Example 1:\nInput: s = {s}, t = {t}\nOutput: {output} ==>", findTheDifference(s, t))

#Boundary Example 2:
#Input: s = "xyz", t = "zyxw"  # Randomly added 'w'
#Output: "w"
s = "xyz"
t = "zyxw"
output = "w"
print(f"#Boundary Example 2:\nInput: s = {s}, t = {t}\nOutput: {output} ==>", findTheDifference(s, t))
