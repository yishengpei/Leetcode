#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        need, window = Counter(s1), Counter()
        left, right, valid = 0, 0, 0

        while right < len(s2):
            c = s2[right]
            right += 1

            if need[c]:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
        
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1
                if need[d]:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return False
# @lc code=end

