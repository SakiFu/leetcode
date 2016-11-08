#Given an integer, write a function to determine if it is a power of three.

#Follow up:
#Could you do it without using any loop / recursion?

#Credits:
#Special thanks to @dietpepsi for adding this problem and creating all test cases.

class Solution(object):
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        elif n%3 or n <= 0:
            return False
        ls = []
        while n:
            n = n/3
            ls.append(n)
        print ls
        for item in ls:
            if item%3 and item>1:
                return False
        return True