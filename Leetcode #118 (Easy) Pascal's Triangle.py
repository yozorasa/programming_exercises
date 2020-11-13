#Leetcode #118 (Easy) Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows > 0:
            ans = []
            for i in range(numRows):
                line = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        line.append(1)
                    else:
                        line.append(ans[i-1][j-1] + ans[i-1][j])
                ans.append(line)
            return ans
        else:
            return []
                
            