class Solution(object):
    def majorityElement(self, nums):
        # Using Boyre-More voting algorithm
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = 0 
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            if num != candidate:
                count -= 1
        return candidate
        
