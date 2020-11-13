#Leetcode #217 (Easy) Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for n in nums:
            if n in temp:
                return True
            else:
                temp[n] = 1
        return False