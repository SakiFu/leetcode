# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n <= 1:
            return True
        while n%2 == 0 and n > 2:
            n /= 2
        return n % 2 == 0