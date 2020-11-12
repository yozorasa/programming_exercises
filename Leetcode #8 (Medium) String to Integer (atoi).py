#Leetcode #8 String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        space = 0
        if s[0]==" ":
            for c in s:
                if c == " ":
                    space = space+1
                else:
                    break
        s = s[space:]
        if len(s)==0:
            return 0
        
        if s[0].isdigit() or s[0]=="+" or s[0]=="-" or s[0]==" ":
            ans = 0
            flag = 0
            if s[0]=="+" or s[0]=="-":
                if s[0] == "-":
                    flag = 1
                s = s[1:]
            for num in s:
                if num.isdigit():
                    ans = ans*10+int(num)
                else:
                    break
            if flag == 1:
                ans = -1*ans
            up = pow(2,31)-1
            down = -1*pow(2,31)
            if ans > up:
                return up
            elif ans < down:
                return down
            else:
                return ans
        else:
            return 0
