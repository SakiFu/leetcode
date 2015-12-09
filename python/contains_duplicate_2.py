# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.


class Solution(object):
    def contains_duplicate(self, nums, k):
        ndict = {}
        for i, num in enumerate(nums):
            if num not in ndict:
                ndict[num] = i
            else:
                if i - ndict[num] <= k:
                    return True
                ndict[num] = i
        return False