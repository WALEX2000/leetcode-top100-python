#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp_nums = nums[:]
        counter = 0
        counter_0 = 0
        for color in tmp_nums:
            nums.pop()
            if color == 0:
                nums.insert(0,0)
                counter_0 += 1
            elif color == 2:
                nums.insert(counter, 2)
            elif color == 1:
                nums.insert(counter_0, 1)
            counter += 1


# @lc code=end

