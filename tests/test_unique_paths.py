FILE_NAME = "62.unique-paths.py"

# This is necessary because importing these weird file names is not straightforward
import importlib.util
from typing import List, Optional
spec = importlib.util.spec_from_file_location(
    name="leetcode_file",
    location=FILE_NAME,
)
leetcode_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(leetcode_file)
Solution = leetcode_file.Solution
# Import end

def test_solution():
    exptected = 28

    result = Solution().uniquePaths(3, 7)

    assert result == exptected

