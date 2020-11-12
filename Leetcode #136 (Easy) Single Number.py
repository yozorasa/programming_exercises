#Leetcode #136 (Easy) Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            if n not in ans:
                ans.append(n)
            else:
                ans.remove(n)
        return ans.pop()