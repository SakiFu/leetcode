# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):
        ls_str = str.split()
        if len(pattern) != len(ls_str):
            return False
        p_tuple = zip(pattern, ls_str)
        p_dict = {}
        s_dict = {}
        for pattern, string in p_tuple:
            if pattern not in p_dict:
                p_dict[pattern] = string
            if string not in s_dict:
                s_dict[string] = pattern
            if s_dict[string] != pattern or p_dict[pattern] != string:
                return False
        return True