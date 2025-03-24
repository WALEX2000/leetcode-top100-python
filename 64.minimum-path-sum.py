#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid_height = len(grid)
        grid_width = len(grid[0])
        
        def explore(x : int, y : int, path_value, min_value : int | None):
            path_value += grid[y][x]
            if x == grid_width - 1 and y == grid_height - 1:
                return path_value

            if y + 1 < grid_height:
                down_value = explore(x,y+1,path_value, min_value)
            else:
                return explore(x+1,y,path_value, min_value)
            
            min_value = down_value if not min_value or down_value < min_value else None
            
            if x + 1 < grid_width:
                right_value = explore(x+1,y,path_value, min_value)
            else:
                return down_value

            return down_value if down_value < right_value else right_value

        return explore(0,0,0, None)

        
# @lc code=end

