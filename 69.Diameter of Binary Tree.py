class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # update diameter at this node
            self.diameter = max(self.diameter, left + right)
            # return height
            return 1 + max(left, right)

        depth(root)
        return self.diameter
# Build tree:   1
#              / \
#             2   3
#            / \
#           4   5

root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3))

sol = Solution()
print("Diameter of tree:", sol.diameterOfBinaryTree(root))
