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
        node = head
        previous_node = None
        while node:
            next_node = node.next
            node.next = previous_node
            previous_node = node
            node = next_node
            if node is head:
                return True

        return False
        
# @lc code=end