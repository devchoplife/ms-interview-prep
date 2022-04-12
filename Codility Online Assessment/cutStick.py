"""
Given a stick of size N, find the number of ways in which it can be cut into K pieces such that length of 
every piece is greater than 0.

Examples : 

Input : N = 15
        K = 5
Output : 1001
"""

def cuts(n, r):
    if (n < r):
        return 0
    
    if (r == 0):
        return 1
    
    # nCr has been simplified to this form by
    # expanding numerator and denominator to
    # the form     n(n - 1)(n - 2)...(n - r + 1)
    #             -----------------------------
    #                         (r!)
    # in the above equation, (n-r)! is cancelled
    # out in the numerator and denominator
    
    numerator = 1
    for i in range(n, n - r, -1):
        numerator = numerator * i
        
    denominator = 1
    for i in range(1, r + 1):
        denominator = denominator * i
    
    return (numerator/denominator)

def countWays(N, K):
    return cuts(N - 1, K - 1)

N = 5
K = 2
print(countWays(N, K))