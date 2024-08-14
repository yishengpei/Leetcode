#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.backtrack(nums,0,track)
        return self.res
    
    def backtrack(self, nums, start, track):
        self.res.append(track[:])
        for i in range(start,len(nums)):
            track.append(nums[i])
            self.backtrack(nums,i+1,track)
            track.pop()
# @lc code=end

