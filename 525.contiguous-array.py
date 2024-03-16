#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = 0

        for i in range(n):
            preSum[i + 1] = preSum[i] + (-1 if nums[i] == 0 else 1)

        valToIndex = {}
        res = 0
        for i in range(len(preSum)):
            if preSum[i] in valToIndex:
                res = max(res, i - valToIndex[preSum[i]])
            else:
                valToIndex[preSum[i]] = i
        return res
# @lc code=end

