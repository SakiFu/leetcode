"""Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2"""


class Solution(object):

    def twoSum(self, nums, target):
        store = {}
        for i in range(len(nums)):
            reminder = target-nums[i]
            if reminder in store:
                return store[reminder] + 1, i + 1
            store[nums[i]] = i
