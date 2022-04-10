"""
Given an array arr[] of N integers, the task is to find all the pairs possible from the given array. 

Note:  
- (arr[i], arr[i]) is also considered as a valid pair.
- (arr[i], arr[j]) and (arr[j], arr[i]) are considered as two different pairs.

Examples: 
Input: arr[] = {1, 2} 
Output: (1, 1), (1, 2), (2, 1), (2, 2).

Input: arr[] = {1, 2, 3} 
Output: (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3) 
"""


def printPairs(arr, n):
    # Nested loop for all possible pairs
    for i in range(n):
        for j in range(n):
            print("(", arr[i], ",", arr[j], ")")


arr = [1, 2]
n = len(arr)

printPairs(arr, n)
