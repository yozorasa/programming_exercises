#Leetcode #344 Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, c  in enumerate(s[:int(len(s)/2)]):
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = c
