FILE_NAME = "39.combination-sum.py"

# This is necessary because importing these weird file names is not straightforward
import importlib.util
spec = importlib.util.spec_from_file_location(
    name="leetcode_file",
    location=FILE_NAME,
)
leetcode_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(leetcode_file)
solution = leetcode_file.Solution()

def test_answer():
    result = solution.combinationSum([2,3,6,7], 7)
    assert result == [[2,2,3],[7]]