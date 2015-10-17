# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        standard = strs[0]
        longest_length = len(standard)
        for string in strs[1:]:
            index = 0
            while index < len(string) and index < len(standard) and string[index] == standard[index]:
                index += 1
            longest_length = min(index, longest_length)
        
        return strs[0][:longest_length]