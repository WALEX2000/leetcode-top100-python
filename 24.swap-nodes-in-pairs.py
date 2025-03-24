#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node: Optional[ListNode], should_swap : bool) -> Optional[ListNode]:
            if not node:
                return None
            
            new_node = swap(node.next, not should_swap)
            if should_swap and new_node:
                prev_next_node = node.next
                prev_next_next_node = node.next.next
                node.next.next = node
                node.next = prev_next_next_node
                return prev_next_node
            else:
                node.next = new_node
            
            return node
        
        return swap(head, True)
        
# @lc code=end

