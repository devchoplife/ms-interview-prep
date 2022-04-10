"""
Given an elevation map, find the maximum amount of water that can be stored within the map (assuming infinite rainfall).

or

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples;
Input: arr[]   = {2, 0, 2}
Output: 2

Explanation:
We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7

Explanation:
We can trap "3 units" of water between 3 and 2,
"1 unit" on top of bar 2 and "3 units" between 2
and 4.  See below diagram also.
"""


def maxWater(arr, n):
    res = 0

    for i in range(1, n - 1):
        # FInd the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the max element on its right
        right = arr[i]

        for j in range(i + 1, n):
            right = max(right, arr[j])

        # Update the max water to hold
        res = res + (min(left, right) - arr[i])

    return res


arr = [0, 1, 0, 2, 1, 0,
       1, 3, 2, 1, 2, 1]
n = len(arr)

print(maxWater(arr, n))
