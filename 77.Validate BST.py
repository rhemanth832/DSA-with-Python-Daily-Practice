class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (isValidBST(root.left, min_val, root.val) and
            isValidBST(root.right, root.val, max_val))
if __name__ == "__main__":
    # ✅ Valid BST
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(7, TreeNode(6), TreeNode(8))

    print("Is Valid BST:", isValidBST(root))  # True

    # ❌ Invalid BST (left child > root)
    root_invalid = TreeNode(5)
    root_invalid.left = TreeNode(6)
    root_invalid.right = TreeNode(7)

    print("Is Valid BST:", isValidBST(root_invalid))  # False
