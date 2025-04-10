#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = int(len(nums) / 2)
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            
            if counter[num] > target:
                return num
# @lc code=end

