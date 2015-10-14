class Solution(object):

    def addDigits(self, num):
        while num >= 10:
            num = sum([int(str(num)[i]) for i in range(len(str(num)))])
        return num