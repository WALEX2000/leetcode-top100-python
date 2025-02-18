#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

from re import sub
from typing import List

# @lc code=start

def generate_subsets(nums: List[int], subset_size: int) -> List[List[int]]:
    subset_list = [nums]

    sub_subset_size = 0
    for i in range(len(nums) - 1, len(nums) - subset_size - 1, -1):
        subset = nums[:i] + nums[i+1:]

        if sub_subset_size > 0:
            subset_list += generate_subsets(subset, sub_subset_size)
        else:
            subset_list.append(subset)
        
        sub_subset_size += 1

    return subset_list

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return generate_subsets(nums, len(nums))
        
# @lc code=end

