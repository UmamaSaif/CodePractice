class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        last = n - 1
        while start <= last:
            middle = (start + last) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                last = middle - 1
            elif nums[middle] < target:
                start = middle + 1
        return -1
