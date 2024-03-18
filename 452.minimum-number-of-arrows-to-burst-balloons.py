#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        count = 1
        x_end = points[0][1]
        for point in points:
            start = point[0]
            if start > x_end:
                count += 1
                x_end = point[1]
        return count
# @lc code=end

