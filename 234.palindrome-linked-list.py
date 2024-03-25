#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next

        left = head
        right = self.reverse(slow)

        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True

    def reverse(self, head: ListNode) -> ListNode:
        pre, cur = None, head

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre
# @lc code=end

