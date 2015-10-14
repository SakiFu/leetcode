class Solution(object):
    def isPalindrome(self, x):
        if 0 < x < 10:
            return True
        else:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False