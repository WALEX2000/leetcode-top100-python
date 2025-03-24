FILE_NAME = "105.construct-binary-tree-from-preorder-and-inorder-traversal.py"

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

def get_tree_values(root : TreeNode) -> List[int]:
    if not root:
        return [None]
    
    values = []
    values.append(root.val)
    values += get_tree_values(root.left)
    values += get_tree_values(root.right)

    return values


def test_basic_problem():
    preorder = [1]
    inorder = [1]
    
    result = Solution().buildTree(preorder, inorder)
    
    assert get_tree_values(result) == [1, None, None]

def test_standard_problem():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    
    result = Solution().buildTree(preorder, inorder)
    
    assert get_tree_values(result) == [3,9,None, None,20,15, None, None,7, None, None]


def test_standard_problem_2():
    preorder = [3,9,10,20,15,7]
    inorder = [10,9,3,15,20,7]
    
    result = Solution().buildTree(preorder, inorder)
    
    assert get_tree_values(result) == [3,9,10,None,None,None,20,15, None, None,7, None, None]
