# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkTree(root: TreeNode) -> bool:
    return (root.right.val + root.left.val) == root.val


class Solution:
    pass


root = [10, 4, 6]
my_tree = TreeNode(root[0], TreeNode(root[1]), TreeNode(root[2]))
# left and right branches are new TreeNode Objects with its values and two branches pointing at None
print(checkTree(my_tree))

root = [5, 3, 1]
my_tree = TreeNode(root[0], TreeNode(root[1]), TreeNode(root[2]))
print(checkTree(my_tree))
