FILE_NAME = "21.merge-two-sorted-lists.py"

# This is necessary because importing these weird file names is not straightforward
import importlib.util
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

def test_2_null_intputs():
    assert Solution().mergeTwoLists(None, None) is None

def test_first_null_input():
    list_1 = None
    list_2 = ListNode(0)

    result = Solution().mergeTwoLists(list_1, list_2)

    assert get_values(result) == [0]

def test_second_null_input():
    list_1 = ListNode(0)
    list_2 = None

    result = Solution().mergeTwoLists(list_1, list_2)

    assert get_values(result) == [0]

def test_simple_solution():
    list_1 = ListNode(1)
    list_2 = ListNode(2, ListNode(3, ListNode(4)))

    result = Solution().mergeTwoLists(list_1, list_2)

    assert get_values(result) == [1,2,3,4]

def test_basic_solution():
    list_1 = ListNode(1, ListNode(2, ListNode(4)))
    list_2 = ListNode(1, ListNode(3, ListNode(4)))

    result = Solution().mergeTwoLists(list_1, list_2)

    assert get_values(result) == [1,1,2,3,4,4]