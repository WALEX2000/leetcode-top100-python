#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List
# @lc code=start

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        correct_combinations = []
        
        def generate_valid_options(option: List[int], candidate: int) -> List[List[int]]:
            valid_permutations = []
            
            option = option.copy()
            option.append(candidate)
            while sum(option) <= target:
                if sum(option) == target:
                    correct_combinations.append(option)
                    return valid_permutations

                valid_permutations.append(option)
                option = option.copy()
                option.append(candidate)
            
            return valid_permutations

        def generate_more_valid_permutations(valid_permutations: List[List[int]], candidate: int) -> List[List[int]]:
            new_permutations = []

            indexes_to_delete = []
            for i, permutation in enumerate(valid_permutations):
                new_valid_options = generate_valid_options(permutation, candidate)
                
                if not new_valid_options:
                    indexes_to_delete.append(i)
                    continue

                new_permutations += new_valid_options
            
            indexes_to_delete.reverse()
            for i in indexes_to_delete:
                valid_permutations.pop(i)
            
            return valid_permutations + new_permutations
        
        valid_permutations = [[]]
        candidates.sort()
        for candidate in candidates:
            valid_permutations = generate_more_valid_permutations(valid_permutations, candidate)

        return correct_combinations

        
# @lc code=end

