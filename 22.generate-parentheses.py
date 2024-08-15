#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        track = ''
        self.backtrack(n,n,track,res)
        return res

    def backtrack(self,left,right,track,res):
        if right < left:
            return 
        if left < 0 or right < 0:
            return 
        if left == 0  and right == 0:
            res.append(track)
            return 
        
        track += '('
        self.backtrack(left-1,right,track,res)
        track = track[:-1]

        track += ')'
        self.backtrack(left,right-1,track,res)
        track = track[:-1]        
# @lc code=end

