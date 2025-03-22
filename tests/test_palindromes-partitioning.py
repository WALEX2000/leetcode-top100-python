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

def test_basic_answer():
    result = solution.partition("aab")
    assert result == [["a","a","b"],["aa","b"]]

def test_aaaa_answer():
    result = solution.partition("aaaa")
    assert result == [['a', 'a', 'a', 'a'], ['aa', 'a', 'a'], ['a', 'aa', 'a'], ['a', 'a', 'aa'], ['aa', 'aa'], ['aaa', 'a'], ['a', 'aaa'], ['aaaa']]
