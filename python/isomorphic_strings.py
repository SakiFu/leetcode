# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.


class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        tupl = zip(s, t)
        sdict = {}
        tdict = {}
        for schar, tchar in tupl:
            if schar not in sdict:
                sdict[schar] = tchar
            if tchar not in tdict:
                tdict[tchar] = schar
            if sdict[schar] != tchar or tdict[tchar] != schar:
                return False
        return True