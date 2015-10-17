#Given an integer n, return the number of trailing zeroes in n!.


class Solution(object):
    def trailingZeroes(self, n):
        fives = 0
        while n > 0:
            fives += n / 5
            n = n / 5
        return fives