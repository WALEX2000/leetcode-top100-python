#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List, Optional
# @lc code=start

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        def sorted_depth_first_search(node: List[int], candidates: List[int]) -> Optional[List[List[int]]]:
            correct_combinations = []
            for index, candidate in enumerate(candidates):
                new_node = node + [candidate]
                if sum(new_node) == target:
                    correct_combinations += [new_node]
                    break
                elif sum(new_node) < target:
                    correct_combinations += sorted_depth_first_search(new_node, candidates[index:])
                else:
                    break

            return correct_combinations

        candidates.sort()
        return sorted_depth_first_search([], candidates)

        
# @lc code=end


