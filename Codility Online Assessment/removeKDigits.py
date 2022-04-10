"""
Given a positive number N, the target is to find the largest number that can be formed after removing any K digits from N.
Examples: 

Input: N = 6358, K = 1 
Output: 658

Input: N = 2589, K = 2 
Output: 89

Approach

- Iterate a loop K times.
- During every iteration, remove every digit from the current value of N once and store the maximum of all the numbers obtained.
- In order to achieve this, we store the maximum of (N / (i * 10)) * i + (N % i) where i ranges from [1, 10l – 1] where l denotes the number of digits of the current value of N.
- Consider this maximum as the current value of N and proceed to the next iteration and repeat the above step.
- Thus, after every iteration, we have the least digit from the current value of N removed. On repeating the process K times, we obtain the largest number possible.
"""


def maxNumber(n, k):
    for i in range(0, k):
        # Generate the largest number after removal of the K digits one by one
        ans = 0
        i = 1

        while n // i > 0:
            # Remove the least digits
            temp = (n // (i * 10)) * i + (n % i)
            i *= 10

            # Compare and store the max
            if temp > ans:
                ans = temp

            n = ans

        return ans


n = 6358
k = 1
print(maxNumber(n, k))
