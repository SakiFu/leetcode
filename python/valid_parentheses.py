"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not."""


class Solution(object):
    def isValid(self, s):
        if s=='':
            return True
        stack=[]
        dict={'}':'{', ']':'[',')':'('}
        
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            elif dict[c]:
                if len(stack)==0:
                    return False
                else:
                    last=stack[-1]
                    if dict[c]!=last:
                        return False
                    else:
                        stack.pop()
            else:
                return False
        return len(stack)==0