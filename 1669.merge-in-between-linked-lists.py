#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1 = node2 = list1
        for _ in range(a - 1):
            node1 = node1.next
        for _ in range(b + 1):
            node2 = node2.next
        
        node3 = list2
        while node3.next:
            node3 = node3.next

        node1.next = list2
        node3.next = node2 

        return list1 
# @lc code=end

