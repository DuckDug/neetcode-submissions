class Solution {
    // int[][] grid2;
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        // grid2 = grid;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                maxArea = Math.max(maxArea, dfs(grid, r, c));
            }
        }
        
        return maxArea;
    }

    private int dfs(int[][] grid, int r, int c) {
        if (r >= grid.length || c >= grid[0].length || r < 0 || c < 0 || grid[r][c] == 0) {
            return 0;
        }
        int count = 1;
        grid[r][c] = 0;
        //up
        count += dfs(grid, r - 1, c);
        //left
        count += dfs(grid, r, c - 1);
        //right
        count += dfs(grid, r, c + 1);
        //down
        count += dfs(grid, r + 1, c);

        return count;
    }
}
