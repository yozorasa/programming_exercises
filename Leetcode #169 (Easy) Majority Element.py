#Leetcode #169 (Easy) Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for i in count.keys():
            if count[i] > len(nums)/2:
                return i
        return 