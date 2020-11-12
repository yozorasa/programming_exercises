#Leetcode #1 Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if numsMap.get(diff) != None:
                return [numsMap.get(diff), i]
            else:
                numsMap[nums[i]] = i