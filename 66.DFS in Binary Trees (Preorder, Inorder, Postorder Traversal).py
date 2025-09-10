# Preorder (Root, Left, Right)
# Inorder (Left, Root, Right)
# Postorder (Left, Right, Root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Traversals defined OUTSIDE the class
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Build tree:   1
#              / \
#             2   3
#            / \
#           4   5

root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3))

print("Preorder :", preorder(root))   # [1, 2, 4, 5, 3]
print("Inorder  :", inorder(root))    # [4, 2, 5, 1, 3]
print("Postorder:", postorder(root))  # [4, 5, 2, 3, 1]


