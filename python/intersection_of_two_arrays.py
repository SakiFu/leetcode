"""Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        if len(nums1) < len(nums2):
            short, long = nums1, nums2
        else:
            short, long = nums2, nums1
        short2 = short[:]
        for i in range(len(short)):
            if short[i] in long:
                long.remove(short[i])
            else:
                short2.remove(short[i])
        return short2