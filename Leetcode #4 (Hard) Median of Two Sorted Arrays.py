#Leetcode #4 Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        medianIdx = int(len(nums)/2)
        if len(nums)%2 != 0:
            return float(nums[medianIdx])
        else:
            return float((nums[medianIdx]+nums[medianIdx-1])/2)
