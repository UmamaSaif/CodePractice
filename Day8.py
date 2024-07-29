class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}

        for index, num in enumerate(nums): #enumerate keeps track of element and its index
            if num in index_map and index - index_map[num] <= k:
                return True
            index_map[num] = index
        return False
        
