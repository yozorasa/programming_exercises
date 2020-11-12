#Leetcode #104 (Easy) Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        def gen(node, n=0):
            if node:
                return max(gen(node.left, n+1),gen(node.right, n+1))
            return n
        return gen(root)  