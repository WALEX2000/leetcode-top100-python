#
# @lc app=leetcode id=2415 lang=python3
#
# [2415] Reverse Odd Levels of Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @lc code=start
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(left_node: TreeNode, right_node: TreeNode, level: int) -> None:
            if left_node is None:
                return
            
            if level % 2 != 0:
                left_node.val, right_node.val = right_node.val, left_node.val

            traverse(left_node.left, right_node.right, level+1)
            traverse(left_node.right, right_node.left, level+1)
        
        traverse(root.left, root.right, 1)
        
        return root
        
# @lc code=end

