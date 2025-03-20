#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generate_next_row(current_row: List[int]) -> List[int]:
            next_row = [1]
            next_row_size = len(current_row) + 1
            items_to_generate = next_row_size - 2

            for i in range(items_to_generate):
                new_item = current_row[i] + current_row[i + 1]
                next_row.append(new_item)
            
            next_row.append(1)
            return next_row

        triangle = [[1]]
        for next_row_index in range(1, numRows):
            current_row = triangle[next_row_index-1]
            triangle.append(generate_next_row(current_row))
        return triangle
# @lc code=end

