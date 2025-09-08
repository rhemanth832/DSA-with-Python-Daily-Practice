# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


# -----------------------------
# Create a linked list:
# 1 -> 2 -> 3 -> 4 -> 2 (cycle back to node with value 2)
# -----------------------------
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2   # cycle here

# Test
solution = Solution()
print(solution.hasCycle(node1))  # Output: True

# Create a list without cycle: 1 -> 2 -> 3 -> None
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)

nodeA.next = nodeB
nodeB.next = nodeC

print(solution.hasCycle(nodeA))  # Output: False
