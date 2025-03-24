#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            result.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue[-1]
                
                if node.right:
                    queue.insert(0,node.right)
                if node.left:
                    queue.insert(0,node.left)
                
                queue.pop()
        
        return result

# @lc code=end

