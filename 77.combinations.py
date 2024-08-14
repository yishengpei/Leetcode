#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
        self.track = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self,start, n, k):
        if k == len(self.track):
            self.res.append(self.track.copy())
            return
        for i in range(start,n+1):
            self.track.append(i)
            self.backtrack(i+1,n,k)
            self.track.pop()
# @lc code=end

