# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(father: TreeNode):
            origin_left = father.left
            origin_right = father.right
            if origin_left is not None:
                father.left = TreeNode(val=-1, left=origin_left)
                dfs(origin_left)
            if origin_right is not None:
                father.right = TreeNode(val=-1, right=origin_right)
                dfs(origin_right)

        dfs(root)
        return root


so = Solution()
