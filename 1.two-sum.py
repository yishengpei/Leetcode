#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in valToIndex:
                return [valToIndex[need], i]
            
            valToIndex[nums[i]] = i
        return []
# @lc code=end

