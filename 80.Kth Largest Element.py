class Solution(object):
    def kthLargest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.right   # go right first (largest values)
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.left
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build BST
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
root.right = TreeNode(6)

print(Solution().kthLargest(root, 2))  # Output: 5 (2nd largest)
#(OR)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort in descending order
        return nums[k - 1]       # Kth largest element


# Example run
nums = [3,2,1,5,6,4]
k = 2
sol = Solution()
print(sol.findKthLargest(nums, k))  # Output: 5
