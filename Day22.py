"""
You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.
"""
class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        sum = 0
       
        for i in range(1, n+1):
            if n % i== 0:
                sum += (nums[i-1] * nums[i-1])
        return sum

        
