from collections import deque
class TreeNode:
    def __init__(self, val=0, left= None, right= None):
        self.val=val
        self.left=left
        self.right=right
def level_order(root):
    if not root:
        return []

    q=deque([root])
    result=[]
    while q:
        node = q.popleft()  # take from front
        result.append(node.val)  # visit node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result
root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3))
print(level_order(root))

