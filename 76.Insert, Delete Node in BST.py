class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert into BST
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    # Search in BST
    def search(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    # Delete node from BST
    def delete(self, root, val):
        if not root:
            return None
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            # Case 1: No child
            if not root.left and not root.right:
                return None
            # Case 2: One child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: Two children
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.delete(root.right, successor.val)
        return root

    # Inorder Traversal (for display)
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

# Example Run
if __name__ == "__main__":
    bst = BST()
    root = None

    # Insert values
    for val in [5, 3, 7, 2, 4, 6, 8]:
        root = bst.insert(root, val)

    print("Inorder Traversal:", bst.inorder(root))

    # Search
    print("Search 4:", "Found" if bst.search(root, 4) else "Not Found")
    print("Search 9:", "Found" if bst.search(root, 9) else "Not Found")

    # Delete
    root = bst.delete(root, 3)
    print("Inorder after deleting 3:", bst.inorder(root))

    root = bst.delete(root, 7)
    print("Inorder after deleting 7:", bst.inorder(root))
