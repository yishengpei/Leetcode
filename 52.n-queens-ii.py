#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.res
    
    def backtrack(self, board, row):
        if row == len(board):
            self.res += 1
            return
        
        for col in range(len(board[row])):
            # 排除不合法选择
            if not self.isValid(board, row, col):
                continue
            # 做选择
            board[row][col] = 'Q'
            # 进入下一行决策
            self.backtrack(board, row + 1)
            # 撤销选择
            board[row][col] = '.'
    
    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        # 检查列是否有皇后互相冲突
        for i in range(row + 1):
            if board[i][col] == 'Q':
                return False
        # 检查右上方是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        # 检查左上方是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
# @lc code=end

