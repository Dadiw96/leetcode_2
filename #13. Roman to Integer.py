#13. Roman to Integer

#Work
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#For example, 2 is written as II in Roman numeral, just two ones added together.
#12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Given a roman numeral, convert it to an integer.

#Rozwiązanie

def romanToInt(s):
    r = 0
    rom = {"I" : 1, "V" : 5, "X": 10, "L":50,
                "C":100, "D":500, "M":1000}
    for i in range(len(s)-1):
        if rom[s[i]] < rom[s[i+1]]:
            r -= rom[s[i]]
        else:
            r += rom[s[i]]  
    return r + rom[s[i+1]]
        
        
        
        

#Example 1:
#Input: s = "III"
#Output: 3
s = "III"
output = 3
print(f"#Example 1:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Example 2:
#Input: s = "LVIII"
#Output: 58
s = "LVIII"
output = 58
print(f"#Example 2:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Example 3:
#Input: s = "MCMXCIV"
#Output: 1994
s = "MCMXCIV"
output = 1994
print(f"#Example 3:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Boundary Example 1:
#Input: s = "I"  # Minimum value
#Output: 1
s = "I"
output = 1
print(f"#Boundary Example 1:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Boundary Example 2:
#Input: s = "MMMCMXCIX"  # Maximum value (3999)
#Output: 3999
s = "MMMCMXCIX"
output = 3999
print(f"#Boundary Example 2:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Boundary Example 3:
#Input: s = "IV"  # Subtractive notation (4)
#Output: 4
s = "IV"
output = 4
print(f"#Boundary Example 3:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Boundary Example 4:
#Input: s = "XL"  # Subtractive notation (40)
#Output: 40
s = "XL"
output = 40
print(f"#Boundary Example 4:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))

#Boundary Example 5:
#Input: s = "XC"  # Subtractive notation (90)
#Output: 90
s = "XC"
output = 90
print(f"#Boundary Example 5:\nInput: s = {s}\nOutput: {output} ==>", romanToInt(s))