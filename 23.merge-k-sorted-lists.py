#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(-1)
        p = dummy

        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))
        while pq:
            node = heapq.heappop(pq)[2]
            p.next = node 
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))

            p = p.next
        return dummy.next

# @lc code=end

