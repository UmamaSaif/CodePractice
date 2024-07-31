# first solution (optimal time complexity)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        n = len(nums)
        numbers = set()
        for i in range(0,n):
            numbers.add(nums[i])
        for i in range(0,n+1):
            if i not in numbers:
                missing = i
        return missing

  # second solution (optimal space complexity)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
  
