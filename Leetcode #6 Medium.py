#Leetcode #6 ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        if numRows==1 or numRows >= len(s):
            ans = s
        else:
            n = numRows*2-2
            for i in range(numRows):
                idx = i
                ans = ans + s[idx]
                while idx < len(s):
                    idx = idx+n-i*2
                    if idx < len(s) and n-i*2!=0:
                        ans = ans + s[idx]
                    idx = idx+i*2
                    if idx < len(s) and i*2!=0:
                        ans = ans + s[idx]
        return ans