class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        res = []

        def dfs(node, level):
            if not node:
                return
            # First time we reach this level → rightmost node
            if level == len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return res


# Output
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(root))  # Output: [1, 3, 4]
