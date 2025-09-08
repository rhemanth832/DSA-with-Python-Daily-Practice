#Built in Commands
from collections import deque
dq = deque()
# Insert
dq.append(10)     # right
dq.append(20)
dq.appendleft(5)  # left
dq.remove(20)     # Delete
print(" -> ".join(map(str, dq)) + " -> None")
 #(OR)
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):   # Insert at end
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_front(self, data): # Insert at beginning
        new = Node(data)
        new.next = self.head
        self.head = new

    def delete(self, key):        # Delete node
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp:
            prev.next = temp.next

    def display(self):            # Print list
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_front(5)
ll.delete(20)
ll.display()   # 5 -> 10 -> None




