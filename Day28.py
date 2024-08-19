"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
"""
class Solution(object):
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums=[]
        for num in nums:
            if num not in unique_nums:
                unique_nums.append(num)
        maximum=0
        if len(unique_nums) >= 3:
            for i in range(0,3):
                if unique_nums:
                    maximum=max(unique_nums)
                while maximum in unique_nums:
                    unique_nums.remove(maximum)
        else:
            if unique_nums:
                return max(unique_nums)
        return maximum

"""
GPT's improved solution
"""
class Solution(object):
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = list(set(nums))  # Remove duplicates by converting to a set
        unique_nums.sort(reverse=True)  # Sort the numbers in descending order
        
        if len(unique_nums) >= 3:
            return unique_nums[2]  # Return the third maximum
        else:
            return unique_nums[0]  # If there are less than 3 unique numbers, return the maximum
     
