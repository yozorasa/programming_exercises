#Leetcode #122 (Easy) Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                ans = ans + prices[i+1] - prices[i]
        return ans
            