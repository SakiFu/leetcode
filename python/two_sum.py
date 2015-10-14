class Solution(object):

    def twoSum(self, nums, target):
        store = {}
        for i in range(len(nums)):
            reminder = target-nums[i]
            if reminder in store:
                return store[reminder] + 1, i + 1
            store[nums[i]] = i
