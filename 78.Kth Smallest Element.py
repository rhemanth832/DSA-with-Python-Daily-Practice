class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build BST
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
root.right = TreeNode(6)

print(Solution().kthSmallest(root, 3))  # Output: 3
