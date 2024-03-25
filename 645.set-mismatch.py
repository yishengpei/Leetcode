#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = -1

        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0:
                dup = abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= -1
        
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
                break
        
        return [dup, missing]
# @lc code=end

