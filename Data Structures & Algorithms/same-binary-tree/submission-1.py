# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(firstNode, secondNode) -> bool:
            if not firstNode and not secondNode:
                return True
            if not firstNode or not secondNode:
                return False
            
            if firstNode.val != secondNode.val:
                return False
            
            return dfs(firstNode.left, secondNode.left) and dfs(firstNode.right, secondNode.right)
        
        return dfs(p,q)