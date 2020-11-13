#Leetcode #121 (Easy) Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            ans = 0
            low = prices[0]
            for i in prices:
                ans = max(i-low, ans)
                low = min(i, low)
            return ans
        else:
            return 0