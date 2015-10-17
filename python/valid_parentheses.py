"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not."""


class Solution(object):
    def isValid(self, s):
        if s == '':
            return True
        stack = []
        dict_p = {'}': '{', ']': '[', ')': '('}

        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            elif dict[p]:
                if len(stack) == 0:
                    return False
                else:
                    last = stack[-1]
                    if dict_p[p] != last:
                        return False
                    else:
                        stack.pop()
            else:
                return False
        return len(stack) == 0