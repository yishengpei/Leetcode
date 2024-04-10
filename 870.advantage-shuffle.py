#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        maxpq = []
        for i in range(n):
            maxpq.append([i,nums2[i]])
        maxpq.sort(key=lambda x:-x[1])

        nums1.sort()

        left, right = 0, n-1
        res = [0] * n

        while maxpq:
            pair = maxpq.pop(0)
            i, maxval = pair[0], pair[1]
            if maxval < nums1[right]:
                res[i] = nums1[right]
                right -=1
            else:
                res[i] = nums1[left]
                left += 1
        return res
# @lc code=end

