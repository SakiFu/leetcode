"""Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""


class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num = sum([int(str(num)[i]) for i in range(len(str(num)))])
        return num