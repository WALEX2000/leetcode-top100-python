FILE_NAME = "114.flatten-binary-tree-to-linked-list.py"

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
TreeNode = leetcode_file.TreeNode
# Import end

def convert_right_tree_to_list_of_values(node: TreeNode) -> List[Optional[int]]:
    if not node:
        return []
    result = [node.val]
    result += convert_right_tree_to_list_of_values(node.right)
    return result

def test_no_output():
    assert Solution().flatten(None) is None

def test_single_node():
    root = TreeNode()
    Solution().flatten(root)
    assert root.left == None and root.right == None

def test_basic_solution():
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))

    Solution().flatten(root)

    assert convert_right_tree_to_list_of_values(root) == [1,2,3,4,5,6]
