"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum=[]
        runningSum.append(nums[0])
        for i in range(1,len(nums)):
            runningSum.append(nums[i]+runningSum[i-1])
        return runningSum
        
