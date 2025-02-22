#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List
# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row_index in range(0, len(matrix)):
            for col_index in range(len(matrix) - 1, -1, -1):
                row = matrix[row_index]
                value = row[len(row) - 1]
                del row[len(row) - 1]
                matrix[col_index] = [value] + matrix[col_index]



        
# @lc code=end

