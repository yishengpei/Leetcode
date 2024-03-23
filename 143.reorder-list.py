#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stk = []

        p = head
        while p != None:
            stk.append(p)
            p = p.next
        
        p = head
        while p != None:
            lastNode = stk.pop()
            next = p.next
            if lastNode == next or lastNode.next == next:
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next
            p = next
            
# @lc code=end

