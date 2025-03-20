#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from typing import List
# @lc code=start

# THIS IS NOT THE OPTIMAL SOLUTION:
# This is my solution, which isn't bad, but for numbers it is possible to use bitwise operations
# Using bitwise operations is much faster and memory efficient
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found_numbers : set[int] = set()
        while len(nums) > 0:
            number = nums[0]
            if number in found_numbers:
                found_numbers.discard(number)
            else:
                found_numbers.add(number)
            
            del nums[0]
        
        return found_numbers.pop()
# @lc code=end

