'''    
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            if target - val in nums and nums.index(target-val) != index:
                return [index, nums.index(target-val)]
