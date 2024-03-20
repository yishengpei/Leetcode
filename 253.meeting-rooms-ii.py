#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        begin = [0] * n
        end = [0] * n
        for i in range(n):
            begin[i] = intervals[i][0]
            end[i] = intervals[i][1]
        
        begin.sort()
        end.sort()

        count = 0
        res, i, j = 0, 0, 0
        while i < n and j < n:
            if begin[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            
            res = max(res, count)
        return res
# @lc code=end

