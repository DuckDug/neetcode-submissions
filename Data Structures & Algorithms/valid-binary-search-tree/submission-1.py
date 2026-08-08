# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, rng):
            if not node:
                return True
            if not rng[0] < node.val < rng[1]:
                return False
            leftRng = [-math.inf, node.val]
            rightRng = [node.val, math.inf]
            return dfs(node.left, [rng[0], node.val]) and dfs(node.right, [node.val, rng[1]])
        
        return dfs(root, [-math.inf, math.inf])