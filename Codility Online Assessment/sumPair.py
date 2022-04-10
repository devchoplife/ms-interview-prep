"""
Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in A[] whose sum is exactly x. 

Examples:
Input: arr[] = {0, -1, 2, -3, 1}
        sum = -2
Output: -3, 1
         Valid pair exists.
"""


def checkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                print("pair with a given sum", x, "is (", A[i], ",", A[j], ")")
                return True

    return False

A = [0, -1, 2, -3, 1]
x = -2
size = len(A)
checkPair(A, size, x)