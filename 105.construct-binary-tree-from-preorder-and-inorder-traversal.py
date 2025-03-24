#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        
        node_value = preorder[0]
        preorder.remove(node_value)

        left_tree_list = None
        right_tree_list = None
        for idx, value in enumerate(inorder):
            if value == node_value:
                left_tree_list = inorder[:idx]
                right_tree_list = inorder[idx+1:]
        
        left_node = self.buildTree(preorder, left_tree_list)
        right_node = self.buildTree(preorder, right_tree_list)

        return TreeNode(node_value, left_node, right_node)

        
# @lc code=end
