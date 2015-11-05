# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        if len(nums) <= 2:
            return nums[0]
        ndict = {}
        for num in nums:
            if num not in ndict:
                ndict[num] = 1
            else:
                ndict[num] += 1
                if ndict[num] > len(nums) /2:
                    return num