#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start

def generate_permutations(current_set: List[int], remaining_set: List[int]) -> List[List[int]]:
    permutations = []
    for i in range(0, len(remaining_set)):
        number = remaining_set[i]
        next_remaining_set = remaining_set[:i] + remaining_set[i+1:]
        permutations += generate_permutations(current_set + [number], next_remaining_set)
    
    if len(remaining_set) == 0:
        permutations.append(current_set)

    return permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return generate_permutations([], nums)
        
# @lc code=end

