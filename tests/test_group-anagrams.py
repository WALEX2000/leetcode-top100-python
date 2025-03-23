FILE_NAME = "49.group-anagrams.py"

# This is necessary because importing these weird file names is not straightforward
import importlib.util
spec = importlib.util.spec_from_file_location(
    name="leetcode_file",
    location=FILE_NAME,
)
leetcode_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(leetcode_file)
solution = leetcode_file.Solution()
# Import end

from functools import reduce

def test_basic_answer():
    CORRECT = [set(["bat"]),set(["nat","tan"]),set(["ate","eat","tea"])]
    result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    assert len(result) == len(CORRECT) and reduce(lambda acc, i: acc & (set(i) in CORRECT), result, True)
