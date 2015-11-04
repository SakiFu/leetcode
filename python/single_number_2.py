# Given an array of integers, every element appears three times except for one. Find that single one.


class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        for num in dict:
            if dict[num] == 1:
                return num