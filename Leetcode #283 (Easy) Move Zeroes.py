#Leetcode #283 (Easy) Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i, n in enumerate(nums):
            nums[i-count] = nums[i]
            if n == 0:
                count = count+1
        for i in range(count):
            nums[len(nums)-1-i] = 0
        return