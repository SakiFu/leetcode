"""Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""


class Solution(object):
    def isAnagram(self, s, t):

        if sorted(s) == sorted(t):
            return True
        else:
            return False