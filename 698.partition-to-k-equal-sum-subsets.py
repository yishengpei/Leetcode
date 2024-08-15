#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):
            return False
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        used = 0
        target = total_sum // k
        return self.backtrack(k,0,nums,0,used,target)
    
    def __init__(self) -> None:
        self.memo = {}

    def backtrack(self, k, bucket, nums, start, used, target):
        if k == 0:
            return True

        if bucket == target:
            res = self.backtrack(k-1, 0, nums, 0, used, target)
            self.memo[used] = res
            return res
        
        if used in self.memo:
            return self.memo[used]
        
        for i in range(start, len(nums)):
            if (used >> i) & 1 == 1:
                # nums[i] 已经被装入别的桶中
                continue
            if nums[i] + bucket > target:
                continue
            # 做选择
            # 将第 i 位置为 1
            used |= 1 << i
            bucket += nums[i]
            # 递归穷举下一个数字是否装入当前桶
            if self.backtrack(k, bucket, nums, i + 1, used, target):
                return True
            # 撤销选择
            # 将第 i 位置为 0
            used ^= 1 << i
            bucket -= nums[i]

        return False
# @lc code=end

