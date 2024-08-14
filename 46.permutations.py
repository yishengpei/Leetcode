#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        used = [False] * len(nums)

        self.backtrack(nums, track, used)

        return self.res

    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            track.append(nums[i])
            used[i] = True

            self.backtrack(nums,track,used)
            track.pop()
            used[i] = False
# @lc code=end

