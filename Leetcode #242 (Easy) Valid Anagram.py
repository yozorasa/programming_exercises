#Leetcode #242 (Easy) Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = collections.Counter(s)
        countT = collections.Counter(t)
        if countS == countT:
            return True
        return False