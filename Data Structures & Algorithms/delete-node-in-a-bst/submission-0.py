# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        def remove(root, key): 
            if not root:
                return None
            
            if root.val < key:
                root.right = remove(root.right, key)
            elif root.val > key:
                root.left = remove(root.left, key)
            else: 
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    minNodeVal = minNode(root.right)
                    root.val = minNodeVal.val
                    root.right = remove(root.right, minNodeVal.val)
            return root 
        return remove(root, key)
