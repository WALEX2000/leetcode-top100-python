#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        if root.left:
            result = self.inorderTraversal(root.left)
        
        result.append(root.val)
        
        if root.right:
            result += self.inorderTraversal(root.right)
        
        return result
        
# @lc code=end

