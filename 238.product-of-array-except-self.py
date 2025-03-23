#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
# @lc code=start

from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for idx in range(1, len(nums)):
            prev_idx = idx - 1
            result[idx] = result[prev_idx] * nums[prev_idx]

        current = 1
        for idx in range(len(nums) - 2, -1, -1):
            next_idx = idx + 1
            current *= nums[next_idx]
            result[idx] *= current

        return result

# @lc code=end

