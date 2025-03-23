#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = [[root.val]]
        level = [root]
        def bfs(level : List[TreeNode]):
            new_level = []
            new_level_values = []
            
            for node in level:
                if node.left:
                    new_level.append(node.left)
                    new_level_values.append(node.left.val)
                if node.right:
                    new_level.append(node.right)
                    new_level_values.append(node.right.val)
            
            if not new_level:
                return
            
            result.append(new_level_values)
            bfs(new_level)
            
        bfs(level)
        return result
        
# @lc code=end

