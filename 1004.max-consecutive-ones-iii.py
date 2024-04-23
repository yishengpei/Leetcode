#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        window_count = 0
        res = 0
        while right < len(nums):
            if nums[right] == 1:
                window_count += 1
            right += 1

            while right - left - window_count > k:
                if nums[left] == 1:
                    window_count -= 1
                left += 1
            
            res = max(res, right-left)
        return res 
# @lc code=end

