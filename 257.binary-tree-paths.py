#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        if root.left:
            for path in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + "->" + path)
        if root.right:
            for path in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + "->" + path)
        return paths


# @lc code=end

