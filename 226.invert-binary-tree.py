#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
    
    def traverse(self, root):
        if not root:
            return 
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.traverse(root.left)
        self.traverse(root.right)
# @lc code=end

