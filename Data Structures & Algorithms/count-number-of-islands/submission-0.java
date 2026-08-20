
class Solution {
    int islandCount = 0;
    char[][] grid2;
    public int numIslands(char[][] grid) {
        grid2 = grid;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == '1') {
                    countIslands(r, c);
                    islandCount++;
                }
            }
        }
        return islandCount;
    }

    public void countIslands(int r, int c) {
        if (r >= grid2.length || c >= grid2[0].length || r < 0 || c < 0 || grid2[r][c] == '0') {
            return;
        }

        grid2[r][c] = '0';
        //up
            countIslands(r - 1, c);
        
        //left
            countIslands(r, c - 1);
        //right
            countIslands(r, c + 1);
        //down
            countIslands(r + 1, c);
    }
}
