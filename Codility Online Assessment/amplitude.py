"""
Suppose we have a lit of numbers called nums, and have another value k. If we remove k elements from nums, 
then find the minimum of (maximum of nums - minimum of nums).
So, if the input is like nums = [4, 10, 3, 2, 8, 9] k = 3, then the output will be 2, because if we remove 10, 
8 and 9 then maximum is 4, minimum is 2 so difference is 2.

To solve this, we will follow these steps -

- sort the list nums
- p := size of nums - k
- m := (last element of nums) - nums[0]
- for i in range 0 to size of nums - p, do
    - if nums[i + p - 1] - nums[i] < m, then
        - m := nums[i + p - 1] - nums[i]
- return m
"""

def solve(num, k):
    nums = sorted(num)
    p = len(nums) - k
    m = nums[-1] - nums[0]
    
    for i in range(0, len(nums) - p + 1):
        if nums[i + p - 1] - nums[i] < m:
            m = nums[i + p - 1] - nums[i]
    
    return m

nums = [10, 4, 3, 2, 9, 8]
k = 3
print(solve(nums, k))