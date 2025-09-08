# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
#OR

# Define a Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to find middle of linked list
def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Function to create linked list from Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Function to print linked list in 5 -> 10 -> 15 -> None format
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
h = [5, 10, 15, 20, 25]
head = create_linked_list(h)
print("Original Linked List:")
print_linked_list(head)

mid = middleNode(head)
print("\nMiddle Node Value:", mid.val)



