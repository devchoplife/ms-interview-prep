"""
Suppose we have a number n, we have to find the maximum number we can make by inserting 5 anywhere in the number.
So, if the input is like n = 826, then the output will be 8526.

To solve this, we will follow these steps 
- temp := n as a string
- ans := -inf
- for i in range 0 to size of temp, do
    - cand := substring of temp from index 0 to i concatenate '5' concatenate substring of temp from index i to end
    - if i is same as 0 and temp[0] is same as '-', then
    go for the next iteration
    - ans := maximum of ans, and the number cand
- return ans
"""


def largest5(n):
    temp = str(n)
    ans = float('-inf')

    for i in range(len(temp) + 1):
        cand = temp[:i] + '5' + temp[i:]
        if i == 0 and temp[0] == '-':
            continue
        ans = max(ans, int(cand))

    return ans

print(largest5(826))