#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)

        dummy.next = head

        x = self.FindFromEnd(dummy, n+1)
        x.next = x.next.next
        return dummy.next

    def FindFromEnd(self, head, n):
        p1 = head
        p2 = head

        for i in range(n):
            p2 = p2.next

        while p2:
            p1 = p1.next
            p2 = p2.next

        return p1
        
# @lc code=end

