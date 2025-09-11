class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def searchBST(root, val):
    if not root:
        return None
    if root.val==val:
        return root
    elif val<root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
# Example Run
if __name__ == "__main__":
    # Build BST
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)

    # Search values
    result = searchBST(root, 2)
    print(result.val if result else "Not Found")   # Output: 2

    result = searchBST(root, 5)
    print(result.val if result else "Not Found")   # Output: Not Found