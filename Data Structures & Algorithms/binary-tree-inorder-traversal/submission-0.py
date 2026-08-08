# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        

        def inOrderTrav(root, result) -> List[int]:
            if not root:
                return None
            inOrderTrav(root.left, result)
            result.append(root.val)
            inOrderTrav(root.right, result)
            return result
        inOrderTrav(root, result)
        return result