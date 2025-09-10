class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1: return -1   # left subtree not balanced
            right = height(node.right)
            if right == -1: return -1  # right subtree not balanced
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1
# Balanced Tree
root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3))
# Unbalanced Tree
unbalanced = TreeNode(1,
              TreeNode(2,
                  TreeNode(3,
                      TreeNode(4))))
sol = Solution()
print("Is Balanced (root):", sol.isBalanced(root))        # True
print("Is Balanced (unbalanced):", sol.isBalanced(unbalanced))  # False