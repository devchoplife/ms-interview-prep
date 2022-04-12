"""
Given an array arr[] consisting of N positive integers, and an integer K, the task is to 
find the maximum possible even sum of any subsequence of size K. If it is not possible to 
find any even sum subsequence of size K, then print -1.

Examples:
Input: arr[] ={4, 2, 6, 7, 8}, K = 3
Output: 18
Explanation: Subsequence having maximum even sum of size K( = 3 ) is {4, 6, 8}.
Therefore, the required output is 4 + 6 + 8 = 18.

Input: arr[] = {5, 5, 1, 1, 3}, K = 3
Output: -1

Naive Approach: 
The simplest approach to solve this problem to generate all possible subsequences of size K 
from the given array and print the value of the maximum possible even sum the possible 
subsequences of the given array.

Time Complexity: O(K * NK)
Auxiliary Space: O(K)

]Efficient Approach: 
To optimize the above approach the idea is to store all even and odd numbers of the given 
array into two separate arrays and sort both these arrays. Finally, use the Greedy 
technique to calculate the maximum sum even subsequence of size K. Follow the steps 
below to solve the problem:

- Initialize a variable, say maxSum to store the maximum even sum of a subsequence of the given array.
- Initialize two arrays, say Even[] and Odd[] to store all the even numbers and odd numbers of the given array respectively.
- Traverse the given array and store all the even numbers and odd numbers of the given array into Even[] and Odd[] array respectively.
- Sort Even[] and Odd[] arrays.
- Initialize two variables, say i and j to store the index of Even[] and Odd[] array respectively.
- Traverse Even[], Odd[] arrays and check the following conditions:
    - If K % 2 == 1 then increment the value of maxSum by Even[i].
    - Otherwise, increment the value of  maxSum by max(Even[i] + Even[i - 1], Odd[j] + Odd[j - 1]).
- Finally, print the value of maxSum.

Time Complexity: O(N * log N)
Auxiliary Space: O(N)
"""
def evenSumK(arr, N, K):
     
    # If count of elements
    # is less than K
    if (K > N):
        return -1
 
    # Stores maximum
    # even subsequence sum
    maxSum = 0
 
    # Stores Even numbers
    Even = []
 
    # Stores Odd numbers
    Odd = []
 
    # Traverse the array
    for i in range(N):
 
        # If current element
        # is an odd number
        if (arr[i] % 2):
 
            # Insert odd number
            Odd.append(arr[i])
 
        else:
 
            # Insert even numbers
            Even.append(arr[i])
 
    # Sort Odd[] array
    Odd.sort(reverse=False)
 
    # Sort Even[] array
    Even.sort(reverse=False)
 
    # Stores current index
    # Of Even[] array
    i = len(Even) - 1
 
    # Stores current index
    # Of Odd[] array
    j = len(Odd) - 1
 
    while (K > 0):
 
        # If K is odd
        if (K % 2 == 1):
 
            # If count of elements
            # in Even[] >= 1
            if (i >= 0):
 
                # Update maxSum
                maxSum += Even[i]
 
                # Update i
                i -= 1
 
            # If count of elements
            # in Even[] array is 0.
            else:
                return -1
 
            # Update K
            K -= 1
 
        # If count of elements
        # in Even[] and odd[] >= 2
        elif (i >= 1 and j >= 1):
            if (Even[i] + Even[i - 1] <=
                    Odd[j] + Odd[j - 1]):
 
                # Update maxSum
                maxSum += Odd[j] + Odd[j - 1]
 
                # Update j.
                j -= 2
 
            else:
 
                # Update maxSum
                maxSum += Even[i] + Even[i - 1]
 
                # Update i
                i -= 2
 
            # Update K
            K -= 2
 
        # If count of elements
        # in Even[] array >= 2.
        elif (i >= 1):
 
            # Update maxSum
            maxSum += Even[i] + Even[i - 1]
 
            # Update i.
            i -= 2
 
            # Update K.
            K -= 2
 
        # If count of elements
        # in Odd[] array >= 2
        elif (j >= 1):
 
            # Update maxSum
            maxSum += Odd[j] + Odd[j - 1]
 
            # Update i.
            j -= 2
 
            # Update K.
            K -= 2
 
    return maxSum

arr = [2, 4, 10, 3, 5]
N = len(arr)
K = 3
 
print(evenSumK(arr, N, K))