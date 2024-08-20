"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

"""
"""
My solution for which time limit exceeded
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array=[]
        result=[]
        for i in range(len(nums)):
            array.append(i+1)
        for i in range(len(array)):
            if array[i] not in nums:
                result.append(array[i])
        return result
"""
GPT's solution
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all=set(range(1,len(nums)+1))
        return all-set(nums)
