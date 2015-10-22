Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.


class Solution(object):
def plusOne(self, digits):
        temp = str(int(''.join(map(str, digits))) + 1)
        return map(int, list(temp))