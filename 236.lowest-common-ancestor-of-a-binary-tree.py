#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def search_lca(node : TreeNode, p: TreeNode, q: TreeNode) -> tuple[TreeNode, TreeNode]:
            if not node:
                return None, None
            
            match_p = node if node == p else None
            match_q = node if node == q else None
            lca = match_p if match_p else match_q

            found_p, found_q = search_lca(node.left, p, q)
            
            if found_p:
                match_p = found_p
            if found_q:
                match_q = found_q

            if (found_p or found_q) and lca:
                return lca, lca
            elif found_q is not None and found_p == found_q:
                return found_p, found_q
            
            found_p, found_q = search_lca(node.right, p, q)

            if found_p:
                match_p = found_p
            if found_q:
                match_q = found_q

            if (found_p or found_q) and lca:
                return lca, lca
            elif found_q is not None and found_p == found_q:
                return found_p, found_q
            
            if match_p and match_q:
                return node, node

            return match_p, match_q
        
        result, _ = search_lca(root, p, q)
        return result
        
# @lc code=end

