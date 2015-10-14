import re

class Solution(object):
    def lengthOfLastWord(self, s):
        if not re.search('[a-zA-Z]', s):
            return 0
            
        else:
            lst = s.split()
            return len(lst[-1])