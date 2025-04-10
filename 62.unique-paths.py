#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from functools import cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_down = m - 1
        num_right = n - 1
        
        @cache
        def construct_moves(right_moves: int, down_moves: int):
            constructed_moves = 0
            if right_moves == 0 or down_moves == 0:
                return 1
            
            constructed_moves += construct_moves(right_moves-1, down_moves)
            constructed_moves += construct_moves(right_moves, down_moves-1)

            return constructed_moves
        
        return construct_moves(num_right, num_down)
        
# @lc code=end
