"""Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Subscribe to see which companies asked this question"""


class Solution(object):
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            if d.get(num):
                return True
            else:
                d[num] = 1
        return False