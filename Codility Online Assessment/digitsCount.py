"""
Given a number K of length N, the task is to find the smallest possible number that can be 
formed from K of N digits by swapping the digits any number of times. 

Examples: 
Input: N = 15, K = 325343273113434 
Output: 112233333344457 
Explanation: 
The smallest number possible after swapping the digits of the given number is 112233333344457

Input: N = 7, K = 3416781 
Output: 1134678 
"""

def smallestPos(s, n):
    ans = ""
    
    arr = [0] * 10
    
    for i in range(n):
        arr[ord(s[i]) - 48] += 1
        
    for i in range(10):
        for j in range(arr[i]):
            ans = ans + str(i)
            
    return ans

N = 15;
K = "325343273113434";
 
print(smallestPos(K, N))