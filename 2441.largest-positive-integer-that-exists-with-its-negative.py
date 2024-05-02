#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left = 0 
        right = len(nums) - 1

        while nums[left] < 0 and left < right:
            if nums[left] * (-1) == nums[right]:
                return nums[right]
            if nums[left] *(-1) > nums[right]:
                left += 1
            else:
                right -= 1
        
        return -1
# @lc code=end

