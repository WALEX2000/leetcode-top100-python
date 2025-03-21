#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List
# @lc code=start
class Solution:
    def column_is_occupied(self, current_board : List[str], target_column_index : int) -> bool:
            for row in current_board:
                if row[target_column_index] == "Q":
                    return True
            return False
        
    def diagonal_is_occupied(self, current_board : List[str], target_column_index : int) -> bool:
        target_row_index = len(current_board)
        for row_index, row in enumerate(current_board):
            row_difference = target_row_index - row_index
            left_diagonal_column_index = target_column_index - row_difference
            right_diagonal_column_index = target_column_index + row_difference

            if left_diagonal_column_index >= 0:
                if row[left_diagonal_column_index] == "Q":
                    return True
            if right_diagonal_column_index < len(row):
                if row[right_diagonal_column_index] == "Q":
                    return True
        
        return False
    
    def get_next_valid_rows(self, current_board : List[str], n : int) -> List[List[str]]:
        next_valid_rows = []
        next_row = ""
        for column_index in range(n):
            if not self.column_is_occupied(current_board, column_index) and not self.diagonal_is_occupied(current_board, column_index):
                dots_remainign = n - column_index - 1
                next_valid_rows.append(next_row + "Q" + "." * dots_remainign)

            next_row += "."
        
        return next_valid_rows

    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(board: List[str]):
            correct_boards = []
            if len(board) == n:
                correct_boards.append(board)
            else:
                possible_next_rows = self.get_next_valid_rows(board, n)
                for row_option in possible_next_rows:
                    correct_boards += backtracking(board + [row_option])

            return correct_boards

        return backtracking([])


# @lc code=end