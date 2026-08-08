/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

final class TreeInfo {
    boolean balanced;
    int height;

    public TreeInfo(boolean balanced, int height) {
        this.balanced = balanced;
        this.height = height;
    }
}

class Solution {
    public TreeInfo dfs(TreeNode node) {
            if (node == null) {
                return new TreeInfo(true, 0);
            }
            TreeInfo left = dfs(node.left);
            TreeInfo right = dfs(node.right);
            boolean balanced = (left.balanced && right.balanced) 
                && Math.abs(left.height - right.height) <= 1;
            return new TreeInfo(balanced, 1 + Math.max(left.height, right.height));


    }
    public boolean isBalanced(TreeNode root) {

        return dfs(root).balanced;
    }
}
