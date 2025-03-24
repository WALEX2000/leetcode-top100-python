#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        solution, other = (list1, list2) if list1.val <= list2.val else (list2, list1)
        current = solution
        while current.next:
            if other.val < current.next.val:
                prev_current_next = current.next
                current.next = other
                other = prev_current_next
            else:
                current = current.next

        current.next = other
        return solution

        
# @lc code=end

