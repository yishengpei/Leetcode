#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, answer = [1] * n, [1] * n, [1] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i] 

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        for i in range(n):
            if i == 0:
                answer[i] = suffix[i+1]
            elif i == n - 1:
                answer[i] = prefix[i-1]
            else:
                answer[i] = suffix[i+1] * prefix[i-1]
        
        return answer
# @lc code=end

