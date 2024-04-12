#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(height[left], left_max)
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                ans += right_max - height[right]
            
        return ans
# @lc code=end

