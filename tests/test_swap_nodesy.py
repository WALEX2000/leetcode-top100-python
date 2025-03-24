FILE_NAME = "24.swap-nodes-in-pairs.py"

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
ListNode = leetcode_file.ListNode
# Import end

def get_values(head : ListNode):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    return values

def test_no_output():
    assert Solution().swapPairs(None) is None

def test_single_node():
    head = ListNode(1)
    result = Solution().swapPairs(head)
    assert result is head

def test_single_pair_solution():
    head = ListNode(1, ListNode(2))
    result = Solution().swapPairs(head)
    assert get_values(result) == [2,1]


def test_basic_solution():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    result = Solution().swapPairs(head)
    assert get_values(result) == [2,1,4,3]

def test_uneven_solution():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution().swapPairs(head)
    assert get_values(result) == [2,1,4,3,5]
