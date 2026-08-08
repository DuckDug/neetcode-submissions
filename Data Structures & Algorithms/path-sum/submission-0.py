class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            return True
        #check left
        if self.hasPathSum(root.left, targetSum):
            return True
        #check right
        if self.hasPathSum(root.right, targetSum):
            return True
        #both false add back to targetSum
        targetSum += root.val
        return False