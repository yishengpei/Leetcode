#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res,self.dfs(grid,i,j))
                
        return res

    def dfs(self,grid,i,j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j <0 or j >= n:
            return 0
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return self.dfs(grid,i+1,j) + self.dfs(grid,i-1,j) + self.dfs(grid,i,j-1) + self.dfs(grid,i,j+1) +1 
# @lc code=end

