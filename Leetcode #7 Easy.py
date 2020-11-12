#Leetcode #7 Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        if(x<0):
            strX = strX[1:]
        strX = strX[::-1]
        if(x<0):
            strX = "-"+strX
        ans = int(strX)
        
        up = pow(2,31)-1
        down = -1*pow(2,31)
        if ans > up or ans < down:
            return 0
        return ans