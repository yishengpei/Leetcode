#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sum_sum = sum(nums)

        target = sum_sum - x 

        left,right = 0, 0
        window_sum = 0
        max_len = float("-inf")

        while right < n:
            window_sum += nums[right]
            right += 1
            while window_sum > target and left < right:
                window_sum -= nums[left]
                left += 1
            
            if window_sum == target:
                max_len = max(max_len, right-left)

        return -1 if max_len == float("-inf") else n - max_len
# @lc code=end

