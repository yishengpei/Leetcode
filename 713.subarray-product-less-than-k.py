#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        window_product = 1
        count = 0

        while right < len(nums):
            window_product *= nums[right]
            right += 1

            while left < right and window_product >= k:
                window_product /= nums[left]
                left += 1
            
            count += right - left
        
        return count
# @lc code=end

