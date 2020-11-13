#Leetcode #171 (Easy) Excel Sheet Column Number

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for c in s:
            ans = ans*26 + ord(c)-ord("A")+1
        return ans