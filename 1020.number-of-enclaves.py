#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(A) or j == len(A[0]) or A[i][j] == 0:
                return
            A[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i in [0, len(A)-1] or j in [0, len(A[0])-1]:
                    dfs(i, j)
        
        return sum(sum(row) for row in A)
# @lc code=end

