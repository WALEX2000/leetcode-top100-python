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
        def bfs(level : List[TreeNode]) -> List[List[int]]:
            new_level = []
            level_values = []
            
            for node in level:
                if node:
                    level_values.append(node.val)
                    new_level.append(node.left)
                    new_level.append(node.right)
            
            if not new_level:
                return level_values
            else:
                return [level_values] + bfs(new_level)
            
        return bfs([root])
        
# @lc code=end

