#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from __future__ import annotations
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = self.get_valid_options("(", 0, n)
        return combinations
    
    def get_valid_options(self, current_string: str, num_closed_parenthesis: int, num_target_parenthesis: int) -> List[str]:
        if num_closed_parenthesis == num_target_parenthesis:
            return [current_string]
        
        all_options = []

        num_characters = len(current_string)
        num_open_parenthesis = num_characters - num_closed_parenthesis*2
        if num_open_parenthesis + num_closed_parenthesis < num_target_parenthesis:
            all_options += self.get_valid_options(current_string + "(", num_closed_parenthesis, num_target_parenthesis)
        
        if num_open_parenthesis > 0:
            all_options += self.get_valid_options(current_string + ")", num_closed_parenthesis+1, num_target_parenthesis)

        return all_options
# @lc code=end

