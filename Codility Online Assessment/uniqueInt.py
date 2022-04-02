"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input:5
Output: [-4,-2,0,2,4]

Example 2:
Input:3
Output: [-2, 0, 2]

Example 3:
Input:1
Output: [0]
"""
from typing import List


def unique_sum(n: int) -> List[int]:
    result = []

    for i in range(n):
        result.append(i * 2 - n + 1)

    return result


n = int(input())
res = unique_sum(n)
print(' '.join(map(str, res)))
