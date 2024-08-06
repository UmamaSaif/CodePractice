"""
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

Return the integer denoting the number of employees who worked at least target hours.
"""
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        emps = 0
        for num in hours:
            if num >= target:
                emps += 1
        return emps

"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
"""
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count

"""
Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.
"""
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = ""
        for c in words:
            acronym += c[0]
        if acronym == s:
            return True
        else:
            return False

