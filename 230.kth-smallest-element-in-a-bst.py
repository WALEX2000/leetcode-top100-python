#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def get_ordered_nodes(node: Optional[TreeNode]) -> List[TreeNode]:
            traversed_nodes : List[TreeNode] = []
            while node:
                traversed_nodes.insert(0,node)
                node = node.left
            
            return traversed_nodes

        
        traversed_nodes = get_ordered_nodes(root)
        kth_value = None
        for i in range(k):
            if traversed_nodes[i].right:
                new_nodes = get_ordered_nodes(traversed_nodes[i].right)
                traversed_nodes = traversed_nodes[:i+1] + new_nodes + traversed_nodes[i+1:]
            
            kth_value = traversed_nodes[i].val

        return kth_value