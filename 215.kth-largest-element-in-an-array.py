#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
# @lc code=start

from heapq import heapify, nsmallest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [num * -1 for num in nums]
        heapify(nums)
        top_k = nsmallest(k, nums)
        return top_k[-1]*-1
# @lc code=end

