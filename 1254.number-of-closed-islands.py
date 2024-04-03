#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(n):
            self.dfs(grid,0,j)
            self.dfs(grid,m-1,j)
        for i in range(m):
            self.dfs(grid,i,0)
            self.dfs(grid,i,n-1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid,i,j)
        return res
    
    def dfs(self, grid, i,j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return
        if grid[i][j] == 1:
            # 已经是海水了
            return
        # 将 (i, j) 变成海水
        grid[i][j] = 1
        # 淹没上下左右的陆地
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
# @lc code=end

