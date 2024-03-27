#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = 0
        for i in range(1, n + 1):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        for i in range(1, len(preSum)):
            leftSum = preSum[i - 1] - preSum[0]
            rightSum = preSum[n] - preSum[i]
            if leftSum == rightSum:
                return i - 1
        return -1
# @lc code=end

