class Solution:
    '''
    Given an array of integers (positive and negative) find the largest continuous sum.
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # initialize current sum and max sum to the first element
        curr_sum = nums[0]
        max_sum = nums[0]

        # iterate through the remaining elements
        for i in nums[1:]:

            # Find the current largest sum
            curr_sum = max(curr_sum+i, i)

            # Find the total largest sum
            max_sum = max(max_sum, curr_sum)
        return max_sum

