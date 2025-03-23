#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node : TreeNode) -> Optional[TreeNode]:
            if not node:
                return
            
            left_chain_end = dfs(node.left)
            right_chain_end = dfs(node.right)

            old_right = node.right
            if node.left:
                node.right = node.left
            node.left = None
            
            if left_chain_end:
                left_chain_end.right = old_right

            chain_end = right_chain_end if right_chain_end else left_chain_end
            if not chain_end:
                chain_end = node

            return chain_end
        
        dfs(root)
        
# @lc code=end

