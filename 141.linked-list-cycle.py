#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes : set[ListNode] = set()
        node = head
        while node:
            if node in visited_nodes:
                return True
            visited_nodes.add(node)
            node = node.next

        return False
        
# @lc code=end