#Leetcode #13 (Easy) Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        pre = 'I'
        for s in s[::-1]:
            if roman[s] >= roman[pre]:
                ans = ans + roman[s]
            else:
                ans = ans - roman[s]
            pre = s
        return ans