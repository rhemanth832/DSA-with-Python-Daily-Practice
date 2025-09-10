# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.ans
# Tree:      1
#           / \
#          2   3
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().maxPathSum(root))  # Output: 6
