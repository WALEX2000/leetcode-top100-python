FILE_NAME = "131.palindrome-partitioning.py"

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
    result = solution.partition("aab")
    assert result == [["a","a","b"],["aa","b"]]

def test_aaaa_answer():
    CORRECT_ANSWER = [['a', 'a', 'a', 'a'], ['aa', 'a', 'a'], ['a', 'aa', 'a'], ['a', 'a', 'aa'], ['aa', 'aa'], ['aaa', 'a'], ['a', 'aaa'], ['aaaa']]
    
    result = solution.partition("aaaa")
    assert reduce(lambda acc, i: (i in CORRECT_ANSWER) & acc, result, True) and len(result) == len(CORRECT_ANSWER)
