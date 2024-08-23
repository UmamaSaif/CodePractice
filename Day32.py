"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
# My Solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count =0 
        result=[]
        for num in nums:
            if num!=0:
                count+=1
            else:
                result.append(count)
                count=0
        result.append(count)
        return max(result)

# GPT's Solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        
        return max_count
