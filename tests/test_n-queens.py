FILE_NAME = "51.n-queens.py"

# This is necessary because importing these weird file names is not straightforward
import importlib.util
spec = importlib.util.spec_from_file_location(
    name="leetcode_file",
    location=FILE_NAME,
)
leetcode_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(leetcode_file)
solution = leetcode_file.Solution()

def test_basic_answer():
    result = solution.solveNQueens(1)
    assert result == [["Q"]]

def test_empty_answer():
    result = solution.solveNQueens(2)
    assert result == []

def test_empty_answer_2():
    result = solution.solveNQueens(3)
    assert result == []

def test_complex_answer():
    result = solution.solveNQueens(4)
    assert result == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]


def test_column_is_occupied():
    result = solution.column_is_occupied([".Q..","...Q","Q..."], 0)
    assert result == True

def test_column_is_not_occupied():
    result = solution.column_is_occupied([".Q..","...Q","Q..."], 2)
    assert result == False

def test_diagonal_is_occupied():
    result = solution.diagonal_is_occupied([".Q..","...Q","Q..."], 1)
    assert result == True

def test_get_next_valid_boards_none():
    result = solution.get_next_valid_rows(["Q...","...Q",".Q.."], 4)
    assert result == []

def test_get_next_valid_boards_single():
    result = solution.get_next_valid_rows([".Q..","...Q","Q..."], 4)
    assert result == ["..Q."]

def test_get_next_valid_boards_mutiple():
    result = solution.get_next_valid_rows(["Q..."], 4)
    assert result == ["..Q.", "...Q"]

def test_get_next_valid_boards_empty():
    result = solution.get_next_valid_rows([], 3)
    assert result == ["Q..", ".Q.", "..Q"]