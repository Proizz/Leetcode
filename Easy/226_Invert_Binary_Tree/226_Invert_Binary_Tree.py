# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        else:
            root.right, root.left = root.left, root.right
            Solution.invertTree(self, root.right)
            Solution.invertTree(self, root.left)
        return root


root = [10, 4, 6]
s = Solution()
my_tree = TreeNode(root[0], TreeNode(root[1]), TreeNode(root[2]))
# left and right branches are new TreeNode Objects with its values and two branches pointing at None
print(s.invertTree(root=my_tree))

root = [5, 3, 1]
my_tree = TreeNode(root[0], TreeNode(root[1]), TreeNode(root[2]))
print(s.invertTree(root=my_tree))
