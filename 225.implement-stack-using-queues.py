#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start

from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_elem = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_elem = x

    def pop(self) -> int:
        size = len(self.q)

        while size > 2:
            self.q.append(self.q.popleft())
            size -= 1
        self.top_elem = self.q[0]
        self.q.append(self.q.popleft())        
        return self.q.popleft()

    def top(self) -> int:
        return self.top_elem

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

