"""
Given a string str, our task is to find the Largest Alphabetic Character, whose both uppercase and lowercase are present in the string. 
The uppercase character should be returned. If there is no such character then return -1 otherwise print the uppercase letter of the character.
Examples:

Input: str = “admeDCAB” 
Output: D 

Explanation: 
Both the uppercase and lowercase characters for letter D is present in the string and it is also the largest alphabetical character, hence our output is D.

Input: str = “dAeB” 
Output: -1 

Explanation: 
Although the largest character is d in the string but the uppercase version is not present hence the output is -1. 
"""
def largestCharacter(str):
    uppercase = [False] * 26
    lowercase = [False] * 26
    
    # Array for keeping track of both uppercase and lowercase alphabets 
    arr = list(str)
    for c in arr:
        if (c.islower()):
            lowercase[ord(c) - ord('a')] = True
        if (c.isupper()):
            uppercase[ord(c) - ord('A')] = True
            
    # Iterate from the right side of the array to get the largest index char
    for i in range(25, -1, -1):
        if (uppercase[i] and lowercase[i]):
            return chr(i + ord('A')) + ""
        
        
str = "azdmeDCABZ"
print(largestCharacter(str))