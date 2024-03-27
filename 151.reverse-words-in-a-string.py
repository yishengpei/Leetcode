#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sb = []
        # 先清洗一下数据，把多余的空格都删掉
        for c in s:
            if c != ' ':
                # 单词中的字母/数字
                sb.append(c)
            elif sb and sb[-1] != ' ':
                # 单词之间保留一个空格
                sb.append(' ')
        # 末尾如果有空格，清除之
        if sb and sb[-1] == ' ':
            sb.pop()
        
        # 清洗之后的字符串
        chars = sb

        # 进行单词的翻转，先整体翻转
        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        
        n = len(chars)
        reverse(0, n-1)
        
        # 再把每个单词翻转
        start = end = 0
        while end < n:
            if chars[end] == ' ':
                reverse(start, end-1)
                start = end + 1
            end += 1
        
        # 翻转最后一个单词
        reverse(start, n-1)
        
        # 最后得到题目想要的结果
        return "".join(chars)
# @lc code=end

