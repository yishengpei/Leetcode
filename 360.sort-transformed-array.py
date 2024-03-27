#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#

# @lc code=start
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        i, j = 0, len(nums) - 1
        # 如果开口朝上，越靠近对称轴函数值越小
        # 如果开口朝下，越靠近对称轴函数值越大
        p = len(nums) - 1 if a > 0 else 0
        res = [0 for _ in range(len(nums))]
        # 执行合并两个有序数组的逻辑
        while i <= j:
            v1 = self.f(nums[i], a, b, c)
            v2 = self.f(nums[j], a, b, c)
            if a > 0:
                # 如果开口朝上，越靠近对称轴函数值越小
                if v1 > v2:
                    res[p] = v1
                    p -= 1
                    i += 1
                else:
                    res[p] = v2
                    p -= 1
                    j -= 1
            else:
                # 如果开口朝下，越靠近对称轴函数值越大
                if v1 > v2:
                    res[p] = v2
                    p += 1
                    j -= 1
                else:
                    res[p] = v1
                    p += 1
                    i += 1
        return res

    def f(self, x: int, a: int, b: int, c: int) -> int:
        return a*x*x + b*x + c
# @lc code=end

