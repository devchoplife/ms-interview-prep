"""
Give you one sorted array, please put them into n buckets, we need to ensure we get n sub array with approximately equal weights.

Example;
input {1, 2, 3, 4, 5} n = 3
output [[[5],[1,4],[2,3]];
"""


def can_partition(num):
    s = sum(num)
    # If it is an odd number, we cannot have two sets with equal sum
    if s % 2 != 0:
        return False

    return can_partition_recursive(num, s/2, 0)


def can_partition_recursive(num, sum, currentIndex):
    if sum == 0:
        return True

    n = len(num)
    if n == 0 or currentIndex >= n:
        return False

    # Recursive call after choosing number at the currentIndex
    # if the number at the currentIndex exceeds the sum, this should not be processed
    if num[currentIndex] <= sum:
        if(can_partition_recursive(num, sum - num[currentIndex], currentIndex + 1)):
            return True

    # Recursive call after excluding the number at the currentIndex
    return can_partition_recursive(num, sum, currentIndex + 1)


print(can_partition([1, 2, 3, 4, 6]))
