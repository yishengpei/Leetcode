#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
# 注意：python 代码由 chatGPT🤖 根据我的 cpp 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def __init__(self):
        self.res = []

    # 输入棋盘边长 n，返回所有合法的放置
    def solveNQueens(self, n: int) -> List[List[str]]:
        # '.' 表示空，'Q' 表示皇后，初始化空棋盘。
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    # 路径：board 中小于 row 的那些行都已经成功放置了皇后
    # 选择列表：第 row 行的所有列都是放置皇后的选择
    # 结束条件：row 超过 board 的最后一行
    def backtrack(self, board: List[List[str]], row: int) -> None:
        # 触发结束条件
        if row == len(board):
            self.res.append([''.join(row) for row in board])
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

    # 是否可以在 board[row][col] 放置皇后？
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

