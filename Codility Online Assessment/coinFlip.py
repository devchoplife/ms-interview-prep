"""
Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped. 

Examples : 
Input : str = “001”
Output : 1

Minimum number of flips required = 1
We can flip 1st bit from 0 to 1 

Input : str = “0001010111”
Output : 2

Minimum number of flips required = 2
We can flip 2nd bit from 0 to 1 and 9th 
bit from 1 to 0 to make alternate 
string “0101010101”.

Expected time complexity : O(n) where n is length of input string.
"""


def flip(ch):
    return '1' if (ch == '0') else '0'


def getFlipWithStartingChar(str, expected):
    flipCount = 0
    for i in range(len(str)):
        # If current char is not expected increase flip count
        if (str[i] != expected):
            flipCount += 1

        # flip expected char each time
        expected = flip(expected)

    return flipCount


def minFlipToMakeStringAlternate(str):
    return min(getFlipWithStartingChar(str, '0'),
               getFlipWithStartingChar(str, '1'))


str = "0001010111"
print(minFlipToMakeStringAlternate(str))
