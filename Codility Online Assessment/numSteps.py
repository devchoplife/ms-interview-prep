"""
Given a binary string str, the task is to print the numbers of steps required to convert it to one by the following operations: 

- If 'S' is odd add 1 to it.
- If 'S' is even divide it by 2.
"""


def calculate(s):
    if len(s) == 1:
        return 0

    count = 0
    i = len(s) - 1

    while i > 0:
        if s[i] == '0':
            count += 1
            i -= 1
        else:
            count += 1

            while s[i] == '1' and i > 0:
                count += 1
                i -= 1
            if i == 0:
                count += 1
            s = s[:i] + "1" + s[i + 1:]

    return count


s = "10000100000"
print(calculate(s))
